
# config.py

# --- Konfigurasi Jaringan ---
BROADCAST_IP = '255.255.255.255'
HARBOR_IP = '192.168.100.103'
UDP_PORT = 6789

# --- Konfigurasi Perangkat Keras ---
MY_SHIP_CODE = "PLM01"
LCD_I2C_ADDRESS = 0x27
LCD_I2C_PORT = 1
LCD_WIDTH = 20
LCD_HEIGHT = 4
BUZZER_PIN = 17
KEYPAD_ROWS = [21, 20, 16, 12]
KEYPAD_COLS = [1, 7, 8, 25]
KEYPAD_MAP = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]
KEY_UP = 'A'
KEY_DOWN = 'C'
KEY_OK = 'B'
KEY_BACK = 'D'

# --- Konfigurasi Aplikasi & Path ---
DB_PATH = 'DATAGPS/File_datagps.db'
STOP_SCRIPT_PATH = './stopslip.sh'
STATUS_LOG_FILE = "system_status.log"
EMERGENCY_FLAG_FILE = 'emergency_alert.json'
BEEP_CMD_FILE = 'beep.cmd'
EMERGENCY_CMD_FILE = 'send_emergency.cmd'   # Untuk memicu pengiriman darurat
BROADCAST_INTERVAL_SECONDS = 300 # Interval broadcast reguler (300 detik = 5 menit)


SLIP_PROTOCOLS = {
    "SLIP": {
        "script": "./startslip.sh",  # Path ke skrip start AODV lengkap
        "daemon": "slattach"             # Nama proses untuk dicek dengan pgrep
    }
}
