# -*- coding: utf-8 -*-

import sqlite3

def update_data_lokasi(db_file, record_id, data_baru):
    """
    Fungsi untuk mengubah data di tabel catatan_lokasi berdasarkan ID.

    :param db_file: path ke file database SQLite
    :param record_id: ID dari baris yang akan diubah
    :param data_baru: sebuah dictionary berisi data baru
    """
    conn = None  # Inisialisasi koneksi
    try:
        # Membuat koneksi ke database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # ---- MEMBANGUN PERINTAH SQL DENGAN AMAN ----
        # Ini adalah cara yang aman untuk membuat query, menghindari SQL Injection.
        # Daftar kolom yang bisa di-update
        kolom_yang_bisa_diubah = ['nama', 'latitude', 'longitude', 'status', 'gps_date', 'gps_time']
        
        # Siapkan bagian SET dari query
        set_parts = []
        values = []

        for kolom, nilai in data_baru.items():
            if kolom in kolom_yang_bisa_diubah:
                set_parts.append("{}=?".format(kolom)) # Sesuai untuk Python 3.5
                values.append(nilai)

        if not set_parts:
            print("Tidak ada data valid untuk diubah.")
            return

        # Gabungkan semua bagian menjadi satu query utuh
        query = "UPDATE KOORDINAT SET {} WHERE id = ?".format(", ".join(set_parts))
        
        # Tambahkan ID ke akhir list nilai untuk WHERE clause
        values.append(record_id)
        
        # Tampilkan query dan data untuk debugging (opsional)
        print("Executing Query:", query)
        print("With Data:", tuple(values))

        # Eksekusi query dengan data yang sudah disiapkan
        cursor.execute(query, tuple(values))

        # Commit (simpan) perubahan ke database
        conn.commit()
        
        # Periksa apakah ada baris yang berubah
        if cursor.rowcount == 0:
            print("Peringatan: Tidak ada baris yang diubah. Periksa apakah ID {} ada.".format(record_id))
        else:
            print("Sukses! Data dengan ID {} berhasil diubah.".format(record_id))

    except sqlite3.Error as e:
        # Tangani jika ada error dari sqlite
        print("Error saat mengakses database: {}".format(e))
    
    finally:
        # Pastikan koneksi selalu ditutup, meskipun terjadi error
        if conn:
            conn.close()
            print("Koneksi ke database ditutup.")


# ---- CONTOH PENGGUNAAN ----
if __name__ == "__main__":
    
    nama_file_db = 'File_datagps.db'
    id_yang_mau_diubah = 1 # Kita akan mengubah data 'Kantor Pusat' yang punya ID 1

    # Siapkan data baru dalam bentuk dictionary.
    # Anda tidak perlu menyertakan semua kolom, hanya yang ingin diubah saja.
    data_update = {
        'nama': 'PLM02',
        'status': 'T',
        'latitude': -6.175,  # Nilai latitude/lintang baru
        'longitude': 106.853, # Nilai longitude/bujur baru
        'gps_date': '210625',
        'gps_time': '132530'
    }
    
    # Panggil fungsi untuk melakukan update
    update_data_lokasi(nama_file_db, id_yang_mau_diubah, data_update)
