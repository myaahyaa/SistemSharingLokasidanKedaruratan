import sqlite3

def add_columns_to_table():
    conn = None
    try:
        conn = sqlite3.connect('File_datagps.db')
        cursor = conn.cursor()
        print("Connected to SQLite for schema modification.")

        # Tambahkan kolom GPS_DATE (TEXT) dan GPS_TIME (TEXT)
        # Periksa apakah kolom sudah ada sebelum menambahkannya
        cursor.execute("PRAGMA table_info(KOORDINAT);")
        columns = [col[1] for col in cursor.fetchall()]

        if 'GPS_DATE' not in columns:
            cursor.execute("ALTER TABLE KOORDINAT ADD COLUMN GPS_DATE TEXT;")
            print("Column 'GPS_DATE' added successfully.")
        else:
            print("Column 'GPS_DATE' already exists.")

        if 'GPS_TIME' not in columns:
            cursor.execute("ALTER TABLE KOORDINAT ADD COLUMN GPS_TIME TEXT;")
            print("Column 'GPS_TIME' added successfully.")
        else:
            print("Column 'GPS_TIME' already exists.")

        conn.commit()
        print("Database schema updated successfully.")

    except sqlite3.Error as error:
        print("Failed to add columns to table:", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection closed.")

if __name__ == '__main__':
    add_columns_to_table()
