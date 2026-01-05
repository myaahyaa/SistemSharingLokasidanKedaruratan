import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from pad4pi import rpi_gpio
from config import (
    LCD_I2C_ADDRESS, LCD_I2C_PORT, LCD_WIDTH, LCD_HEIGHT,
    KEYPAD_ROWS, KEYPAD_COLS, KEYPAD_MAP, BUZZER_PIN
)

class Hardware:
    def __init__(self):
        self.lcd = CharLCD(
            i2c_expander='PCF8574',
            address=LCD_I2C_ADDRESS,
            port=LCD_I2C_PORT,
            cols=LCD_WIDTH,
            rows=LCD_HEIGHT,
            auto_linebreaks=False
        )
        self.lcd.backlight_enabled = True
        self.lcd.clear()
        
        print("LCD Initialized.")
        
        GPIO.setwarnings(False)
        keypad_factory = rpi_gpio.KeypadFactory()
        self.keypad = keypad_factory.create_keypad(
            keypad=KEYPAD_MAP,
            row_pins=KEYPAD_ROWS,
            col_pins=KEYPAD_COLS
        )
        print("Keypad Initialized.")

        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        print(f"Buzzer Initialized on GPIO {BUZZER_PIN}.")

    def buzzer_on(self):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)

    def buzzer_off(self):
        GPIO.output(BUZZER_PIN, GPIO.LOW)

    def register_key_handler(self, handler_function):
        self.keypad.registerKeyPressHandler(handler_function)

    def cleanup(self):
        self.keypad.cleanup()
        print("Hardware resources cleaned up.")

    def display(self, line1="", line2="", line3="", line4="", clear=True):
        if clear:
            self.lcd.clear()
        self.lcd.cursor_pos = (0, 0)
        self.lcd.write_string(line1.ljust(LCD_WIDTH))
        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string(line2.ljust(LCD_WIDTH))
        self.lcd.cursor_pos = (2, 0)
        self.lcd.write_string(line3.ljust(LCD_WIDTH))
        self.lcd.cursor_pos = (3, 0)
        self.lcd.write_string(line4.ljust(LCD_WIDTH))

    def write_line(self, text, row, col=0, clear_line=False):
        self.lcd.cursor_pos = (row, col)
        if clear_line:
            self.lcd.write_string(' ' * LCD_WIDTH)
            self.lcd.cursor_pos = (row, col)
        self.lcd.write_string(text)

    def create_custom_char(self, location, charmap):
        self.lcd.create_char(location, charmap)
