from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def baratlaut():
    BARATLAUT00 = (
    0b11111,
    0b11111,
    0b11110,
    0b11111,
    0b11011,
    0b10001,
    0b00000,
    0b00000    
    )
    BARATLAUT01 = (
    0b10000,
    0b00000,
    0b00000,
    0b00000,
    0b10000,
    0b11000,
    0b11100,
    0b01110    
    )
    BARATLAUT02 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    BARATLAUT10 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    BARATLAUT11 = (
    0b00111,
    0b00011,
    0b00001,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )
    BARATLAUT12 = (
    0b00000,
    0b10000,
    0b11000,
    0b11100,
    0b01110,
    0b00111,
    0b00011,
    0b00000    
    )
    
    


    lcd.create_char(0, BARATLAUT00)
    lcd.create_char(1, BARATLAUT01)
    lcd.create_char(2, BARATLAUT02)
    lcd.create_char(3, BARATLAUT10)
    lcd.create_char(4, BARATLAUT11)
    lcd.create_char(5, BARATLAUT12)
    #lcd.create_char(6, BARATLAUT20)
    #lcd.create_char(7, BARATLAUT21)
    #lcd.create_char(8, BARATLAUT22)

    lcd.cursor_pos = (0, 17)
    lcd.write_string('\x00')
    lcd.cursor_pos = (0, 18)
    lcd.write_string('\x01')
    lcd.cursor_pos = (0, 19)
    lcd.write_string('\x02')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x03')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x04')
    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x05')
   # lcd.cursor_pos = (2, 17)
   # lcd.write_string('\x02')
   # lcd.cursor_pos = (2, 18)
   # lcd.write_string('\x05')
    #l#cd.cursor_pos = (2, 19)
    #lcd.write_string(0x08)

baratlaut()

