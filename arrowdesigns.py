# arrow_designs.py
# Modul ini berisi kumpulan fungsi untuk menggambar panah navigasi.
# Fungsi draw_northeast telah diubah sesuai dengan kode spesifik Anda.

EMPTY_CHAR = (0,0,0,0,0,0,0,0)

def clear_arrow_area(hw):
    """Membersihkan area grid 3x3 di kanan atas layar."""
    hw.write_line('   ', 0, 17)
    hw.write_line('   ', 1, 17)
    hw.write_line('   ', 2, 17)

def draw_north(hw):
    """Menggambar panah Utara, berdasarkan kode 'utara()' dari Anda."""
    UTARA00=(0,0,0,1,3,7,0,0); UTARA01=EMPTY_CHAR; UTARA02=EMPTY_CHAR
    UTARA10=(4,14,31,31,31,31,14,14); UTARA11=(14,14,14,14,14,14,14,14); UTARA12=UTARA11
    UTARA20=(0,0,0,16,24,28,0,0); UTARA21=EMPTY_CHAR
    hw.lcd.create_char(0,UTARA00); hw.lcd.create_char(1,UTARA01); hw.lcd.create_char(2,UTARA02)
    hw.lcd.create_char(3,UTARA10); hw.lcd.create_char(4,UTARA11); hw.lcd.create_char(5,UTARA12)
    hw.lcd.create_char(6,UTARA20); hw.lcd.create_char(7,UTARA21)
    hw.lcd.cursor_pos = (0, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18); hw.lcd.write_string('\x03')
    hw.lcd.cursor_pos = (0, 19); hw.lcd.write_string('\x06')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x07')
    hw.lcd.cursor_pos = (2, 17); hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (2, 18); hw.lcd.write_string('\x05')

# =======================================================
# == FUNGSI INI DIUBAH SESUAI KODE ANDA ==
def draw_northeast(hw):
    """Menggambar panah Timur Laut, berdasarkan desain spesifik 'timurlaut()' dari Anda."""
    
    # Definisikan 6 potongan karakter dari kode Anda
    TIMURLAUT00 = (0b11111,0b11111,0b01111,0b11111,0b11011,0b10001,0b00000,0b00000)
    TIMURLAUT01 = (0b00001,0b00000,0b00000,0b00000,0b00001,0b00011,0b00111,0b01110)
    TIMURLAUT02 = (0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000)
    TIMURLAUT10 = (0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000)
    TIMURLAUT11 = (0b11100,0b11000,0b10000,0b00000,0b00000,0b00000,0b00000,0b00000)
    TIMURLAUT12 = (0b00000,0b00001,0b00011,0b00111,0b01110,0b11100,0b11000,0b00000)

    # Muat karakter ke memori LCD
    hw.lcd.create_char(0, TIMURLAUT00)
    hw.lcd.create_char(1, TIMURLAUT01)
    hw.lcd.create_char(2, TIMURLAUT02)
    hw.lcd.create_char(3, TIMURLAUT10)
    hw.lcd.create_char(4, TIMURLAUT11)
    hw.lcd.create_char(5, TIMURLAUT12)
    
    # Tampilkan karakter di posisi yang Anda tentukan
    hw.lcd.cursor_pos = (0, 19)
    hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18)
    hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (0, 17)
    hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (1, 19)
    hw.lcd.write_string('\x03')
    hw.lcd.cursor_pos = (1, 18)
    hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 17)
    hw.lcd.write_string('\x05')
# =======================================================

def draw_east(hw):
    """Menggambar panah Timur, berdasarkan desain spesifik 'timur()' dari Anda."""
    TIMUR00 = (0,0,0,0,0,0,0,16); TIMUR01 = (24,28,30,31,30,28,24,16)
    TIMUR02 = (0,0,31,31,31,0,0,0); TIMUR03 = TIMUR02
    hw.lcd.create_char(4, TIMUR00); hw.lcd.create_char(5, TIMUR01)
    hw.lcd.create_char(6, TIMUR02); hw.lcd.create_char(7, TIMUR03)
    hw.lcd.cursor_pos = (0, 19); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x05')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x06')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x07')

def draw_southeast(hw):
    """Menggambar panah Tenggara, berdasarkan desain spesifik 'tenggara()' dari Anda."""
    TENGGARA00 = (0,24,28,14,7,3,1,0); TENGGARA01 = (0,0,0,0,0,16,24,28)
    TENGGARA02 = EMPTY_CHAR; TENGGARA10 = EMPTY_CHAR
    TENGGARA11 = (14,7,3,0,0,0,0,1); TENGGARA12 = (0,0,17,27,31,15,31,31)
    hw.lcd.create_char(0, TENGGARA00); hw.lcd.create_char(1, TENGGARA01)
    hw.lcd.create_char(2, TENGGARA02); hw.lcd.create_char(3, TENGGARA10)
    hw.lcd.create_char(4, TENGGARA11); hw.lcd.create_char(5, TENGGARA12)
    hw.lcd.cursor_pos = (0, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18); hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (0, 19); hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x03')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x05')

def draw_south(hw):
    """Menggambar panah Selatan, berdasarkan desain spesifik 'selatan()' dari Anda."""
    SELATAN00 = EMPTY_CHAR; SELATAN12 = (14,14,14,14,14,14,14,14)
    SELATAN20 = (0,0,7,3,1,0,0,0); SELATAN21 = (14,14,31,31,31,31,14,4)
    SELATAN22 = (0,0,28,24,16,0,0,0)
    hw.lcd.create_char(0, SELATAN00); hw.lcd.create_char(4, SELATAN12)
    hw.lcd.create_char(5, SELATAN20); hw.lcd.create_char(6, SELATAN21); hw.lcd.create_char(7, SELATAN22)
    hw.lcd.cursor_pos = (0, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (0, 19); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (2, 17); hw.lcd.write_string('\x05')
    hw.lcd.cursor_pos = (2, 18); hw.lcd.write_string('\x06')
    hw.lcd.cursor_pos = (2, 19); hw.lcd.write_string('\x07')

def draw_southwest(hw):
    """Menggambar panah Barat Daya. Berdasarkan desain spesifik BaratDaya"""
    BARATDAYA00 = (0,3,7,14,28,24,16,0)
    BARATDAYA01 = (0,0,0,0,0,1,3,7)
    BARATDAYA02 = EMPTY_CHAR
    BARATDAYA10 = EMPTY_CHAR
    BARATDAYA11 = (14,28,24,16,0,0,0,16)
    BARATDAYA12 = (0,0,17,27,31,30,31,31)
    
    hw.lcd.create_char(0, BARATDAYA00)
    hw.lcd.create_char(1, BARATDAYA01)
    hw.lcd.create_char(2, BARATDAYA02)
    hw.lcd.create_char(3, BARATDAYA10)
    hw.lcd.create_char(4, BARATDAYA11)
    hw.lcd.create_char(5, BARATDAYA12)

    hw.lcd.cursor_pos = (0, 19)
    hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18)
    hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (0, 17)
    hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (1, 19)
    hw.lcd.write_string('\x03')
    hw.lcd.cursor_pos = (1, 18)
    hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 17)
    hw.lcd.write_string('\x05')

    
def draw_west(hw):
    """Menggambar panah Barat, berdasarkan desain spesifik 'barat()' dari Anda."""
    BARAT00 = (0,0,0,0,0,0,0,1); BARAT01 = (3,7,15,31,15,7,3,1)
    BARAT02 = (0,0,31,31,31,0,0,0); BARAT10 = BARAT02
    hw.lcd.create_char(0, BARAT00); hw.lcd.create_char(1, BARAT01)
    hw.lcd.create_char(2, BARAT02); hw.lcd.create_char(3, BARAT10)
    hw.lcd.cursor_pos = (0, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x03')

def draw_northwest(hw):
    """Menggambar panah Barat Laut, berdasarkan desain spesifik 'baratlaut()' dari Anda."""
    BARATLAUT00 = (31,31,30,31,27,17,0,0); BARATLAUT01 = (16,0,0,0,16,24,28,14)
    BARATLAUT02 = EMPTY_CHAR; BARATLAUT10 = EMPTY_CHAR
    BARATLAUT11 = (7,3,1,0,0,0,0,0); BARATLAUT12 = (0,16,24,28,14,7,3,0)
    hw.lcd.create_char(0, BARATLAUT00); hw.lcd.create_char(1, BARATLAUT01)
    hw.lcd.create_char(2, BARATLAUT02); hw.lcd.create_char(3, BARATLAUT10)
    hw.lcd.create_char(4, BARATLAUT11); hw.lcd.create_char(5, BARATLAUT12)
    hw.lcd.cursor_pos = (0, 17); hw.lcd.write_string('\x00')
    hw.lcd.cursor_pos = (0, 18); hw.lcd.write_string('\x01')
    hw.lcd.cursor_pos = (0, 19); hw.lcd.write_string('\x02')
    hw.lcd.cursor_pos = (1, 17); hw.lcd.write_string('\x03')
    hw.lcd.cursor_pos = (1, 18); hw.lcd.write_string('\x04')
    hw.lcd.cursor_pos = (1, 19); hw.lcd.write_string('\x05')
