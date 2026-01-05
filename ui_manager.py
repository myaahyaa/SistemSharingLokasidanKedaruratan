from config import LCD_WIDTH, MY_SHIP_CODE, KEY_UP, KEY_DOWN, KEY_OK, KEY_BACK
import arrowdesigns

def draw_emergency_screen(hw, ship_name, blink_on):
    hw.lcd.backlight_enabled = blink_on
    
    line1 = "DARURAT!!".center(LCD_WIDTH)
    line2 = f"KAPAL {ship_name}".center(LCD_WIDTH)
    line3 = ""
    line4 = "0 = keluar".center(LCD_WIDTH)

    hw.display(line1, line2, line3, line4, clear=False)

def draw_destination_select_layout(hw):
    hw.lcd.clear()
    hw.write_line("Pilih Tujuan :", 0)
    hw.write_line(f"{KEY_UP}=^ {KEY_DOWN}=v {KEY_OK}=OK {KEY_BACK}=Batal", 3)

def update_destination_select_data(hw, target_ship_data, scroll_offset=0):
    _, nama, lat, lintang, lon, bujur, status, _, _ = target_ship_data
    status_text = status or "UNKNOWN"
    nama_tampil = (nama or '')[:9]
    status_tampil = status_text[:9]

    line2 = f"{str(lat or '-'):<8} {str(lintang or ''):<1} {nama_tampil}"
    line3 = f"{str(lon or '-'):<8} {str(bujur or ''):<1} {status_tampil}"
    hw.write_line(line2, 1, clear_line=True)
    hw.write_line(line3, 2, clear_line=True)

def draw_navigation_screen(hw, own_ship_data, target_ship_data, distance, bearing):
    hw.lcd.clear()
    
    _, _, own_lat, own_lin, own_lon, own_buj, _, _, _ = own_ship_data
    _, target_nama, _, _, _, _, _, _, _ = target_ship_data

    lat_str = f"{own_lat:.3f}" if own_lat is not None else "---.---"
    lon_str = f"{own_lon:.3f}" if own_lon is not None else "---.---"
    bearing_str = f"{int(bearing)}" if bearing is not None else "---"
    nama_tampil = (target_nama or "")[:7]

    if distance is not None:
        if distance > 99.999:
            dist_str = "99.99+km"
        else:
            dist_str = f"{distance:.3f}km"
    else:
        dist_str = "---.---km"

    split_col = 10
    num_width = 7

    left1 = "POSISI"
    right1= "ARAH"

    left2 = f"{lat_str:<{num_width}} {own_lin or ' '}"
    right2 = nama_tampil
    
    left3 = f"{lon_str:<{num_width}} {own_buj or ' '}"
    right3 = "Jarak:"
    
    line1 = f"{left1:<{split_col}}{right1}"
    line2 = f"{left2:<{split_col}}{right2}"
    line3 = f"{left3:<{split_col}}{right3}"
    line4 = f"{KEY_BACK}=Menu {dist_str:>6} {bearing_str}d"
    
    hw.write_line(line1, 0)
    hw.write_line(line2, 1)
    hw.write_line(line3, 2)
    hw.write_line(line4, 3)
    
    b = bearing if bearing is not None else -1
    
    if 345 <= b or b < 15:
        arrowdesigns.draw_north(hw)
    elif 15 <= b < 75:
        arrowdesigns.draw_northeast(hw)
    elif 75 <= b < 105:
        arrowdesigns.draw_east(hw)
    elif 105 <= b < 165:
        arrowdesigns.draw_southeast(hw)
    elif 165 <= b < 195:
        arrowdesigns.draw_south(hw)
    elif 195 <= b < 255:
        arrowdesigns.draw_southwest(hw)
    elif 255 <= b < 285:
        arrowdesigns.draw_west(hw)
    elif 285 <= b < 345:
        arrowdesigns.draw_northwest(hw)
    else:
        arrowdesigns.clear_arrow_area(hw)

def draw_main_menu(hw, menu_options, selected_index):
    lines = ["", "", "", ""]
    for i, option in enumerate(menu_options):
        if i < 3:
            selector = "> " if i == selected_index else "  "
            lines[i] = f"{selector}{option}"
            
    lines[3] = f"{KEY_UP}=^ {KEY_DOWN}=v {KEY_OK}=OK"
    hw.display(lines[0], lines[1], lines[2], lines[3])
