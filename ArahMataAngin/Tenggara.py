from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def tenggara():
    TENGGARA00 = (
    0b00000,
    0b11000,
    0b11100,
    0b01110,
    0b00111,
    0b00011,
    0b00001,
    0b00000    
    )
    TENGGARA01 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b10000,
    0b11000,
    0b11100    
    )
    TENGGARA02 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    TENGGARA10 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
    TENGGARA11 = (
    0b01110,
    0b00111,
    0b00011,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00001
    )
    TENGGARA12 = (
    0b00000,
    0b00000,
    0b10001,
    0b11011,
    0b11111,
    0b01111,
    0b11111,
    0b11111    
    )
    
    


    lcd.create_char(0, TENGGARA00)
    lcd.create_char(1, TENGGARA01)
    lcd.create_char(2, TENGGARA02)
    lcd.create_char(3, TENGGARA10)
    lcd.create_char(4, TENGGARA11)
    lcd.create_char(5, TENGGARA12)
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

tenggara()

