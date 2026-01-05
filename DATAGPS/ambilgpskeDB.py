import sqlite3
import serial
import time
import pynmea2

# Konfigurasi port serial GPS
port = '/dev/ttyUSB0' # Pastikan ini adalah port yang benar untuk GPS Anda
baud = 9600

# Fungsi untuk mengkonversi koordinat dari format NMEA (DDMM.MMMM) ke Derajat Desimal
def convert_nmea_to_decimal(nmea_coord):
    """
    Mengkonversi koordinat GPS dari format DDMM.MMMM ke Derajat Desimal.
    Contoh: '1234.5678' (12 derajat, 34.5678 menit) menjadi 12.57613
    """
    nmea_coord_float = float(nmea_coord)
    degrees = int(nmea_coord_float / 100)
    minutes = nmea_coord_float % 100
    decimal_degrees = degrees + (minutes / 60)
    return round(decimal_degrees, 9) # Pembulatan untuk presisi

# Fungsi untuk memperbarui tabel SQLite
# Lebih baik melewatkan nilai sebagai argumen daripada menggunakan variabel global
def updateSqliteTable(latitude, lintang_dir, longitude, bujur_dir):
    nama = 'PLM02'
    conn = None # Inisialisasi conn di luar try block
    try:
        conn = sqlite3.connect('File_datagps.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        # Pastikan nama kolom di tabel KOORDINAT sudah benar (LATITUDE, LINTANG, LONGITUDE, BUJUR, NAMA)
        cursor.execute('UPDATE KOORDINAT set LATITUDE = ?, LINTANG = ?, LONGITUDE = ?, BUJUR = ? WHERE NAMA = ?',
                       (latitude, lintang_dir, longitude, bujur_dir, nama))

        conn.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table:", error) # Perbaiki format print error
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

# Inisialisasi port serial
try:
    serialPort = serial.Serial(port, baudrate=baud, timeout=0.5)
    print(f"Serial port {port} opened successfully.")
except serial.SerialException as e:
    print(f"Error opening serial port {port}: {e}")
    print("Please check if the device is connected and the port is correct.")
    exit() # Keluar dari program jika port serial tidak bisa dibuka

print("Starting GPS data acquisition...")
while True:
    nmea_sentence = ''
    try:
        # Membaca satu baris dari serial dan decode
        nmea_sentence = serialPort.readline().decode('utf-8', errors='ignore').strip()
    except Exception as e:
        # Menampilkan error yang sebenarnya
        print(f"Error reading serial data: {e}")

    # Hanya proses jika ada data yang terbaca
    if nmea_sentence:
        print(f"Raw NMEA: {nmea_sentence}")

        # Periksa apakah kalimat NMEA adalah GGA
        if 'GGA' in nmea_sentence:
            try:
                msg = pynmea2.parse(nmea_sentence)

                # Pastikan msg adalah objek GGA sebelum mengakses atribut spesifik
                if isinstance(msg, pynmea2.types.talker.GGA):
                    print(f"Timestamp: {msg.timestamp}, Latitude: {msg.lat} {msg.lat_dir}, Longitude: {msg.lon} {msg.lon_dir}, Altitude: {msg.altitude}, Satellites: {msg.num_sats}")

                    # Konversi lintang dan bujur ke format derajat desimal
                    lati_decimal = convert_nmea_to_decimal(msg.lat)
                    long_decimal = convert_nmea_to_decimal(msg.lon)

                    print(f"Latitude Decimal: {lati_decimal}")
                    print(f"Longitude Decimal: {long_decimal}")
                    print(f"Latitude Direction: {msg.lat_dir}")
                    print(f"Longitude Direction: {msg.lon_dir}")

                    # Panggil fungsi update dengan nilai yang sudah dikonversi
                    updateSqliteTable(lati_decimal, msg.lat_dir, long_decimal, msg.lon_dir)
                else:
                    print(f"Parsed sentence is not GGA: {type(msg)}")

            except pynmea2.ParseError as e:
                print(f"NMEA Parse Error: {e} - Sentence: {nmea_sentence}")
            except Exception as e:
                print(f"An unexpected error occurred during parsing or update: {e}")
        # else:
        #     # Anda bisa mengaktifkan ini jika ingin melihat semua kalimat NMEA yang tidak GGA
        #     # print(f"Skipping non-GGA sentence: {nmea_sentence}")
    else:
        print("No NMEA data received or incomplete line.")

    time.sleep(1)
