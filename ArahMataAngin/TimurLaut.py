from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def timurlaut():
    TIMURLAUT00 = (
    0b11111,
    0b11111,
    0b01111,
    0b11111,
    0b11011,
    0b10001,
    0b00000,
    0b00000
    )
    TIMURLAUT01 = (
    0b00001,
    0b00000,
    0b00000,
    0b00000,
    0b00001,
    0b00011,
    0b00111,
    0b01110    
    )
    TIMURLAUT02 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    TIMURLAUT10 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    TIMURLAUT11 = (
    0b11100,
    0b11000,
    0b10000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )
    TIMURLAUT12 = (
    0b00000,
    0b00001,
    0b00011,
    0b00111,
    0b01110,
    0b11100,
    0b11000,
    0b00000    
    )
    
    


    lcd.create_char(0, TIMURLAUT00)
    lcd.create_char(1, TIMURLAUT01)
    lcd.create_char(2, TIMURLAUT02)
    lcd.create_char(3, TIMURLAUT10)
    lcd.create_char(4, TIMURLAUT11)
    lcd.create_char(5, TIMURLAUT12)

    lcd.cursor_pos = (0, 19)
    lcd.write_string('\x00')
    lcd.cursor_pos = (0, 18)
    lcd.write_string('\x01')
    lcd.cursor_pos = (0, 17)
    lcd.write_string('\x02')
    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x03')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x04')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x05')
   # lcd.cursor_pos = (2, 17)
   # lcd.write_string('\x02')
   # lcd.cursor_pos = (2, 18)
   # lcd.write_string('\x05')
    #l#cd.cursor_pos = (2, 19)
    #lcd.write_string(0x08)

timurlaut()

