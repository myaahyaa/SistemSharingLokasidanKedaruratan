import sqlite3
from config import DB_PATH

def setup_database():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS KOORDINAT (
            ID INTEGER PRIMARY KEY,
            NAMA TEXT UNIQUE NOT NULL,
            LATITUDE REAL,
            LINTANG TEXT,
            LONGITUDE REAL,
            BUJUR TEXT,
            STATUS TEXT,
            GPS_DATE TEXT,
            GPS_TIME TEXT
        )
        ''')
        conn.commit()
        print("Database setup complete (Schema 9 Kolom).")
    except sqlite3.Error as e:
        print(f"Error saat setup database: {e}")
    finally:
        if conn:
            conn.close()

def get_ship_by_id(ship_id):
    record = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM KOORDINAT WHERE ID = ?", (ship_id,))
        record = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error saat membaca data kapal by ID: {e}")
    finally:
        if conn:
            conn.close()
    return record

def get_own_ship_data():
    return get_ship_by_id(1)

def get_all_neighbor_ships():
    records = []
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM KOORDINAT WHERE ID > 1 ORDER BY NAMA ASC")
        records = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error saat membaca data kapal tetangga: {e}")
    finally:
        if conn:
            conn.close()
    return records

def update_or_insert_neighbor(nama, lat, lintang, lon, bujur, status, gps_date, gps_time):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO KOORDINAT (NAMA, LATITUDE, LINTANG, LONGITUDE, BUJUR, STATUS, GPS_DATE, GPS_TIME)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(NAMA) DO UPDATE SET
                LATITUDE=excluded.LATITUDE,
                LINTANG=excluded.LINTANG,
                LONGITUDE=excluded.LONGITUDE,
                BUJUR=excluded.BUJUR,
                STATUS=excluded.STATUS,
                GPS_DATE=excluded.GPS_DATE,
                GPS_TIME=excluded.GPS_TIME;
        ''', (nama, lat, lintang, lon, bujur, status, gps_date, gps_time))

        conn.commit()
        print(f"Data kapal '{nama}' telah disimpan/diperbarui.")
    except sqlite3.Error as e:
        print(f"Error saat menyimpan data tetangga: {e}")
    finally:
        if conn:
            conn.close()

def update_own_ship_position(lat, lintang, lon, bujur, status, gps_date, gps_time):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE KOORDINAT SET LATITUDE=?, LINTANG=?, LONGITUDE=?, BUJUR=?, STATUS=?, GPS_DATE=?, GPS_TIME=?
            WHERE ID = 1
        ''', (lat, lintang, lon, bujur, status, gps_date, gps_time))
        conn.commit()
        print(f"Posisi OWN-SHIP diperbarui: Lat={lat}, Lon={lon}")
    except sqlite3.Error as e:
        print(f"Error saat memperbarui posisi OWN-SHIP: {e}")
    finally:
        if conn:
            conn.close()

