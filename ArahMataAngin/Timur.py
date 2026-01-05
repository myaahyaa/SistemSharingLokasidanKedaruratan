from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)

def timur():

    TIMUR00 = (
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b10000
    )
    TIMUR01 = (
        0b11000,
        0b11100,
        0b11110,
        0b11111,
        0b11110,
        0b11100,
        0b11000,
        0b10000
    )
    TIMUR02 = (
        0b00000,
        0b00000,
        0b11111,
        0b11111,
        0b11111,
        0b00000,
        0b00000,
        0b00000
    )
    TIMUR03 = (
        0b00000,
        0b00000,
        0b11111,
        0b11111,
        0b11111,
        0b00000,
        0b00000,
        0b00000
    )

    lcd.create_char(4, TIMUR00)
    lcd.create_char(5, TIMUR01)
    lcd.create_char(6, TIMUR02)
    lcd.create_char(7, TIMUR03)

    #print to lcd
    lcd.cursor_pos = (0, 19)
    lcd.write_string('\x04')

    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x05')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x06')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x07')

timur()
