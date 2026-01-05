# booting.py
# Versi yang dikembalikan ke rata kiri (tanpa center) dan tanpa verifikasi daemon.

import time
import subprocess
from config import SLIP_PROTOCOLS, STOP_SCRIPT_PATH, LCD_WIDTH

def run(hw, choice):
    """
    Menjalankan dan memverifikasi proses booting dengan tampilan rata kiri,
    tanpa verifikasi daemon routing.
    """
    hw.lcd.clear()
    
    protocols_name = choice
    try:
        protocol_config = SLIP_PROTOCOLS[choice]
    except KeyError:
        print(f"Error: Konfigurasi untuk '{protocols_name}' tidak ditemukan di config.py")
        return False

    # --- Tahap 1: Jalankan Skrip ---
    hw.write_line(f"Menjalankan Protocol", 0)
    hw.write_line(f"{protocols_name}...".center(20), 1)

    try:
        subprocess.run(["/bin/bash", STOP_SCRIPT_PATH], check=True, timeout=10)
        time.sleep(1)
        subprocess.Popen(["/bin/bash", protocol_config["script"]])
        time.sleep(4)
    except Exception as e:
        print(f"Error saat menjalankan script: {e}")
        hw.write_line("Gagal Jalankan Script", 2)
        time.sleep(4)
        return False

    # --- Tahap 2: Verifikasi Sistem ---
    hw.write_line("Mempersiapkan Sistem", 0, clear_line=True)
    hw.write_line("", 1, clear_line=True) # Hapus baris kedua
    time.sleep(1)

    # Verifikasi Antarmuka SLIP
    slip_ready = False
    try:
        subprocess.run(['ifconfig', 'sl0'], check=True, capture_output=True, timeout=5)
        hw.write_line("-> SLIP Interface OK", 2)
        slip_ready = True
    except Exception:
        hw.write_line("-> SLIP Interface GAGAL", 2)
    time.sleep(2)

    # --- Tahap 3: Hasil Akhir ---
    hw.lcd.clear()
    if slip_ready:
        hw.write_line("Sistem Ready".center(20), 1)
        time.sleep(2)
        return True
    else:
        hw.write_line("Sistem Gagal".center(20), 1)
        time.sleep(4)
        return False
