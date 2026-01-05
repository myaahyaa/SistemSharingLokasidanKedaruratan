from RPLCD import i2c
#from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
#lcd.backlight_enabled = False 


def selatan():
    SELATAN00 = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000    
    )
             
    SELATAN12 = (
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110
    )
    SELATAN20 = (
    0b00000,
    0b00000,
    0b00111,
    0b00011,
    0b00001,
    0b00000,
    0b00000,
    0b00000    
    )
    SELATAN21 = (
    0b01110,
    0b01110,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100    
    )
    SELATAN22 = (
    0b00000,
    0b00000,
    0b11100,
    0b11000,
    0b10000,
    0b00000,
    0b00000,
    0b00000    
    )


    lcd.create_char(0, SELATAN00)
  #  lcd.create_char(1, SELATAN01)
   # lcd.create_char(2, SELATAN02)
  #  lcd.create_char(3, SELATAN10)
   # lcd.create_char(4, SELATAN11)
    lcd.create_char(4, SELATAN12)
    lcd.create_char(5, SELATAN20)
    lcd.create_char(6, SELATAN21)
    lcd.create_char(7, SELATAN22)

    lcd.cursor_pos = (0, 17)
    lcd.write_string('\x00')
    lcd.cursor_pos = (0, 18)
    lcd.write_string('\x04')
    lcd.cursor_pos = (0, 19)
    lcd.write_string('\x00')
    lcd.cursor_pos = (1, 17)
    lcd.write_string('\x00')
    lcd.cursor_pos = (1, 18)
    lcd.write_string('\x04')
    lcd.cursor_pos = (1, 19)
    lcd.write_string('\x00')
    lcd.cursor_pos = (2, 17)
    lcd.write_string('\x05')
    lcd.cursor_pos = (2, 18)
    lcd.write_string('\x06')
    lcd.cursor_pos = (2, 19)
    lcd.write_string('\x07')



selatan()
