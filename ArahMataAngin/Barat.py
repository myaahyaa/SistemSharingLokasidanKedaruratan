from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def barat():
    BARAT00 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00001
    )
    BARAT01 = (
    0b00011,
    0b00111,
    0b01111,
    0b11111,
    0b01111,
    0b00111,
    0b00011,
    0b00001    
    )
    BARAT02 = (
    0b00000,
    0b00000,
    0b11111,
    0b11111,
    0b11111,
    0b00000,
    0b00000,
    0b00000
   
    )
    BARAT10 = (
    0b00000,
    0b00000,
    0b11111,
    0b11111,
    0b11111,
    0b00000,
    0b00000,
    0b00000    
    )
    
    lcd.create_char(0, BARAT00)
    lcd.create_char(1, BARAT01)
    lcd.create_char(2, BARAT02)
    lcd.create_char(3, BARAT10)
   # lcd.create_char(4, BARAT11)
    #lcd.create_char(5, BARAT12)
    #lcd.create_char(6, BARAT20)
    #lcd.create_char(7, BARAT21)
    #lcd.create_char(8, BARAT22)

    lcd.cursor_pos = (0, 17)
    lcd.write_string('\x00')
   # lcd.cursor_pos = (0, 18)
   # lcd.write_string('\x03')
   # lcd.cursor_pos = (0, 19)
   # lcd.write_string('\x06')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x01')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x02')
    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x03')
  #  lcd.cursor_pos = (2, 17)
   # lcd.write_string('\x02')
   # lcd.cursor_pos = (2, 18)
   # lcd.write_string('\x05')
    #l#cd.cursor_pos = (2, 19)
    #lcd.write_string(0x08)
barat()
#barat(kode_barat)

