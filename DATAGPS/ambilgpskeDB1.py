import sqlite3
import serial
import time
import pynmea2
import datetime

# ==============================================================================
# KONFIGURASI
# ==============================================================================

# Konfigurasi port serial GPS
# Linux: '/dev/ttyUSB0', '/dev/ttyAMA0', dll.
# Windows: 'COM3', 'COM4', dll.
# Pastikan ini adalah port yang benar untuk GPS Anda
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Konfigurasi Database
DB_FILE = 'File_datagps.db'
DEVICE_NAME = 'PLM01' # Nama perangkat yang akan diupdate di database

# ==============================================================================
# FUNGSI-FUNGSI
# ==============================================================================

def convert_nmea_to_decimal(nmea_coord):
    """
    Mengkonversi koordinat GPS dari format NMEA (DDMM.MMMM) ke Derajat Desimal.
    Contoh: '1234.5678' (12 derajat, 34.5678 menit) menjadi 12.57613
    """
    if not nmea_coord:
        return 0.0
    try:
        nmea_coord_float = float(nmea_coord)
        degrees = int(nmea_coord_float / 100)
        minutes = nmea_coord_float % 100
        decimal_degrees = degrees + (minutes / 60)
        return round(decimal_degrees, 6) # Pembulatan 6 angka di belakang koma untuk presisi
    except (ValueError, TypeError):
        return 0.0

def update_sqlite_table(latitude, lat_dir, longitude, lon_dir, date_str, time_str):
    """
    Menyambungkan ke database SQLite dan memperbarui record dengan data GPS terbaru.
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Perintah SQL UPDATE untuk mengubah data berdasarkan NAMA
        # Pastikan nama kolom (LATITUDE, LINTANG, LONGITUDE, BUJUR, TANGGAL, WAKTU, NAMA)
        # sesuai dengan yang ada di tabel KOORDINAT Anda.
        sql_query = '''UPDATE KOORDINAT 
                       SET LATITUDE = ?, LINTANG = ?, LONGITUDE = ?, BUJUR = ?, GPS_DATE = ?, GPS_TIME = ? 
                       WHERE NAMA = ?'''
        
        data_tuple = (latitude, lat_dir, longitude, lon_dir, date_str, time_str, DEVICE_NAME)
        
        cursor.execute(sql_query, data_tuple)
        
        # Cek apakah ada baris yang berhasil diupdate
        if cursor.rowcount == 0:
            print(f"WARNING: No record found for NAMA='{DEVICE_NAME}'. Please insert a record first.")
        else:
            conn.commit()
            print(f"SUCCESS: Record for '{DEVICE_NAME}' updated -> Tgl: {date_str}, Waktu: {time_str}, Lat: {latitude}, Lon: {longitude}")
        
        cursor.close()

    except sqlite3.Error as error:
        print(f"DATABASE ERROR: Failed to update sqlite table: {error}")
    finally:
        if conn:
            conn.close()

# ==============================================================================
# PROGRAM UTAMA
# ==============================================================================

if __name__ == "__main__":
    # Inisialisasi port serial
    serial_port = None
    try:
        serial_port = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1.0)
        print(f"Serial port {SERIAL_PORT} opened successfully at {BAUD_RATE} baud.")
    except serial.SerialException as e:
        print(f"SERIAL ERROR: Error opening serial port {SERIAL_PORT}: {e}")
        print("Please check if the device is connected and the port is correct.")
        exit()

    print("Starting GPS data acquisition... (Press Ctrl+C to stop)")
    
    last_known_date = None # Variabel untuk menyimpan tanggal terakhir dari kalimat RMC

    try:
        while True:
            try:
                # Membaca satu baris dari serial dan melakukan decode
                line = serial_port.readline().decode('utf-8', errors='ignore').strip()

                # Hanya proses jika ada data yang terbaca
                if line:
                    # Mencari kalimat RMC untuk mendapatkan informasi TANGGAL
                    # Kalimat RMC adalah sumber utama untuk data tanggal yang andal.
                    if 'RMC' in line:
                        try:
                            msg = pynmea2.parse(line)
                            if isinstance(msg, pynmea2.RMC) and msg.datestamp:
                                last_known_date = msg.datestamp
                        except pynmea2.ParseError:
                            continue # Abaikan jika parsing RMC gagal, lanjut ke baris berikutnya

                    # Mencari kalimat GGA untuk informasi LOKASI dan WAKTU
                    # GGA memberikan data posisi, ketinggian, dan jumlah satelit yang lebih detail.
                    if 'GGA' in line:
                        try:
                            msg = pynmea2.parse(line)
                            # Pastikan pesan adalah GGA dan memiliki data yang valid (bukan kosong)
                            if isinstance(msg, pynmea2.GGA) and msg.lat and msg.lon and msg.timestamp:
                                
                                # Cek apakah kita sudah punya data tanggal dari RMC
                                if last_known_date is None:
                                    print("Waiting for valid RMC sentence to get date...")
                                    time.sleep(1)
                                    continue # Lompati iterasi ini jika tanggal belum didapat

                                # Konversi lintang dan bujur ke format derajat desimal
                                lati_decimal = convert_nmea_to_decimal(msg.lat)
                                long_decimal = convert_nmea_to_decimal(msg.lon)

                                # Format tanggal dan waktu ke dalam string standar
                                date_string = last_known_date.strftime('%Y-%m-%d') # Format: YYYY-MM-DD
                                time_string = msg.timestamp.strftime('%H:%M:%S')   # Format: HH:MM:SS (UTC)

                                # Panggil fungsi untuk memperbarui database
                                update_sqlite_table(lati_decimal, msg.lat_dir, long_decimal, msg.lon_dir, date_string, time_string)
                                
                                # Jeda setelah berhasil update untuk menghindari update beruntun yang terlalu cepat
                                time.sleep(5) 

                        except pynmea2.ParseError as e:
                            print(f"NMEA PARSE ERROR: {e} - Sentence: {line}")

            except serial.SerialException as e:
                print(f"SERIAL COMMUNICATION ERROR: {e}. Attempting to reconnect...")
                time.sleep(5) # Tunggu 5 detik sebelum mencoba lagi
            except Exception as e:
                print(f"An unexpected error occurred in the main loop: {e}")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    finally:
        if serial_port and serial_port.is_open:
            serial_port.close()
            print("Serial port closed.")
