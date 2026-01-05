from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def utara():
    UTARA00 = (
    0b00000,
    0b00000,
    0b00000,
    0b00001,
    0b00011,
    0b00111,
    0b00000,
    0b00000
    )
    UTARA01 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )
    UTARA02 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )
    UTARA10 = (
    0b00100,
    0b01110,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b01110
    )
    UTARA11 = (
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110
    )
    UTARA12 = (
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110
    )
    UTARA20 = (
    0b00000,
    0b00000,
    0b00000,
    0b10000,
    0b11000,
    0b11100,
    0b00000,
    0b00000
    )
    UTARA21 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )
    UTARA22 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
    )


    lcd.create_char(0, UTARA00)
    lcd.create_char(1, UTARA01)
    lcd.create_char(2, UTARA02)
    lcd.create_char(3, UTARA10)
    lcd.create_char(4, UTARA11)
    lcd.create_char(5, UTARA12)
    lcd.create_char(6, UTARA20)
    lcd.create_char(7, UTARA21)
    #lcd.create_char(8, UTARA22)

    lcd.cursor_pos = (0, 17)
    lcd.write_string('\x00')
    lcd.cursor_pos = (0, 18)
    lcd.write_string('\x03')
    lcd.cursor_pos = (0, 19)
    lcd.write_string('\x06')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x01')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x04')
    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x07')
    lcd.cursor_pos = (2, 17)
    lcd.write_string('\x02')
    lcd.cursor_pos = (2, 18)
    lcd.write_string('\x05')
    #l#cd.cursor_pos = (2, 19)
    #lcd.write_string(0x08)

utara()

