import time
import sys
import subprocess
import os
import json

from config import KEY_UP, KEY_DOWN, KEY_OK, KEY_BACK, STOP_SCRIPT_PATH, EMERGENCY_FLAG_FILE, EMERGENCY_CMD_FILE, BEEP_CMD_FILE
from hardware import Hardware

import db_manager
import booting
import ui_manager
import math_utils

class AppState:
    BOOTING, DESTINATION_SELECT, NAVIGATION, MAIN_MENU = 1, 20, 30, 40
    EMERGENCY_ALERT = 99

current_state = AppState.BOOTING
last_key_press = None
menu_options = ["Pilih Tujuan", "Kembali"]
menu_index = 0
neighbor_ships = []
destination_index = 0
target_ship_id = None
full_redraw_needed = True

def key_pressed_handler(key):
    global last_key_press
    last_key_press = key
    print(f"Key '{key}' pressed.")

def handle_destination_select(hw):
    global current_state, last_key_press, neighbor_ships, destination_index
    global target_ship_id, full_redraw_needed
    if full_redraw_needed:
        ui_manager.draw_destination_select_layout(hw)
        neighbor_ships = db_manager.get_all_neighbor_ships()
        if not neighbor_ships:
            hw.write_line("Tidak ada tujuan", 1, clear_line=True); hw.write_line("tersedia.", 2, clear_line=True)
            time.sleep(2)
            full_redraw_needed = True; current_state = AppState.NAVIGATION; return
        full_redraw_needed = False
    
    if last_key_press:
        key = last_key_press; last_key_press = None
        if key == KEY_DOWN: destination_index = (destination_index + 1) % len(neighbor_ships)
        elif key == KEY_UP: destination_index = (destination_index - 1) % len(neighbor_ships)
        elif key == KEY_BACK: full_redraw_needed = True; current_state = AppState.NAVIGATION; return
        elif key == KEY_OK:
            target_ship_id = neighbor_ships[destination_index][0]
            full_redraw_needed = True; current_state = AppState.NAVIGATION; return
    ui_manager.update_destination_select_data(hw, neighbor_ships[destination_index])

def handle_navigation_screen(hw):
    global current_state, last_key_press, target_ship_id, full_redraw_needed
    if last_key_press == KEY_BACK:
        last_key_press = None
        global menu_index; menu_index = 0
        full_redraw_needed = True; current_state = AppState.MAIN_MENU; return
    own_ship_data = db_manager.get_own_ship_data()
    if target_ship_id is None: target_ship_id = 2
    target_ship_data = db_manager.get_ship_by_id(target_ship_id)
    if not own_ship_data or not target_ship_data:
        hw.display(line2="Data kapal hilang.", line3="Cek database/target."); time.sleep(2)
        full_redraw_needed = True; current_state = AppState.DESTINATION_SELECT; return
    dist = math_utils.calculate_distance(own_ship_data[2], own_ship_data[4], target_ship_data[2], target_ship_data[4])
    bearing = math_utils.calculate_bearing(own_ship_data[2], own_ship_data[4], target_ship_data[2], target_ship_data[4])
    ui_manager.draw_navigation_screen(hw, own_ship_data, target_ship_data, dist, bearing)

def handle_main_menu(hw):
    global current_state, last_key_press, menu_index, full_redraw_needed
    if full_redraw_needed:
        ui_manager.draw_main_menu(hw, menu_options, menu_index)
        full_redraw_needed = False
        
    if last_key_press:
        key = last_key_press; last_key_press = None
        if key == KEY_DOWN:
            menu_index = (menu_index + 1) % len(menu_options)
        elif key == KEY_UP:
            menu_index = (menu_index - 1) % len(menu_options)
        elif key == KEY_OK:
            full_redraw_needed = True
            selected_option = menu_options[menu_index]

            if selected_option == "Pilih Tujuan":
                destination_index = 0; neighbor_ships = []
                current_state = AppState.DESTINATION_SELECT
            
            elif selected_option == "Kembali":
                current_state = AppState.NAVIGATION
        
        if current_state == AppState.MAIN_MENU:
                ui_manager.draw_main_menu(hw, menu_options, menu_index)

def handle_emergency_alert(hw):
    global current_state, last_key_press, full_redraw_needed
    emergency_data = {}
    try:
        with open(EMERGENCY_FLAG_FILE, 'r') as f:
            emergency_data = json.load(f)
    except Exception as e:
        print(f"Error membaca file darurat: {e}.")
        if os.path.exists(EMERGENCY_FLAG_FILE): os.remove(EMERGENCY_FLAG_FILE)
        current_state = AppState.NAVIGATION
        full_redraw_needed = True
        return

    ship_name = emergency_data.get("nama", "UNKNOWN")
    
    blink_state = True
    last_blink_time = time.monotonic()
    
    hw.buzzer_on()
    hw.lcd.backlight_enabled = True

    while True:
        if last_key_press == '0':
            last_key_press = None
            print("Keluar dari mode darurat...")
            
            hw.buzzer_off()
            hw.lcd.backlight_enabled = True
            
            if os.path.exists(EMERGENCY_FLAG_FILE):
                os.remove(EMERGENCY_FLAG_FILE)
                
            current_state = AppState.NAVIGATION
            full_redraw_needed = True
            return

        if not os.path.exists(EMERGENCY_FLAG_FILE):
            print("File flag darurat dihapus. Keluar dari mode darurat.")
            hw.buzzer_off()
            hw.lcd.backlight_enabled = True
            current_state = AppState.NAVIGATION
            full_redraw_needed = True
            return

        current_time = time.monotonic()
        if (current_time - last_blink_time) >= 0.5:
            blink_state = not blink_state
            last_blink_time = current_time

            ui_manager.draw_emergency_screen(hw, ship_name, blink_state)
            if blink_state:
                hw.buzzer_on()
            else:
                hw.buzzer_off()
        
        time.sleep(0.01)

if __name__ == "__main__":
    hw = None
    try:
        hw = Hardware(); hw.register_key_handler(key_pressed_handler)
        db_manager.setup_database()
        
        while True:
            if os.path.exists(BEEP_CMD_FILE):
                hw.buzzer_on()
                time.sleep(0.1)
                hw.buzzer_off()
                try:
                    os.remove(BEEP_CMD_FILE)
                except OSError as e:
                    print(f"Gagal menghapus file beep: {e}")
            
            if last_key_press == '5':
                print("TOMBOL 5 DITEKAN: Memicu pengiriman sinyal darurat...")
                with open(EMERGENCY_CMD_FILE, 'w') as f: pass
                last_key_press = None
                hw.display(line2="SINYAL DARURAT", line3="   DIKIRIMKAN..."); time.sleep(2)
                full_redraw_needed = True
            
            if os.path.exists(EMERGENCY_FLAG_FILE):
                if current_state != AppState.EMERGENCY_ALERT:
                    print("INTERUPSI DARURAT TERDETEKSI!"); current_state = AppState.EMERGENCY_ALERT
            
            if current_state == AppState.EMERGENCY_ALERT:
                handle_emergency_alert(hw)
            
            elif current_state == AppState.BOOTING:
                boot_success = booting.run(hw, "SLIP")
                if boot_success:
                    print("Boot successful. Defaulting to neighbor 2. State: NAVIGATION.")
                    target_ship_id = 2
                    current_state = AppState.NAVIGATION
                else:
                    print("Boot failed. Program berhenti.")
                    hw.display(line2="BOOTING GAGAL", line3="CEK LOG & RESTART")
                    while True: time.sleep(1)
                full_redraw_needed = True

            elif current_state == AppState.DESTINATION_SELECT:
                handle_destination_select(hw)
            elif current_state == AppState.NAVIGATION:
                handle_navigation_screen(hw)
            elif current_state == AppState.MAIN_MENU:
                handle_main_menu(hw)
            
            if current_state == AppState.NAVIGATION: time.sleep(1)
            elif current_state != AppState.EMERGENCY_ALERT: time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    except Exception as e:
        print(f"\nTerjadi error fatal: {e}")
    finally:
        if hw:
            print("INFO: Stopping all routing services...")
            try:
                subprocess.run(["/bin/bash", STOP_SCRIPT_PATH], check=True, capture_output=True)
                print("INFO: Routing services stopped successfully.")
            except Exception as e: print(f"WARNING: Failed to execute stop_routing.sh: {e}")
            if os.path.exists(EMERGENCY_CMD_FILE): os.remove(EMERGENCY_CMD_FILE)
            if os.path.exists(EMERGENCY_FLAG_FILE): os.remove(EMERGENCY_FLAG_FILE)
            if os.path.exists(BEEP_CMD_FILE): os.remove(BEEP_CMD_FILE)
            hw.display(line2="   SHUTTING DOWN"); time.sleep(1.5)
            hw.lcd.clear(); hw.lcd.backlight_enabled = False
            hw.cleanup()
        print("Program selesai."); sys.exit(0)
