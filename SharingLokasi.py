import socket
import time
import threading
import json
import os
import db_manager
import config

db_lock = threading.Lock()

def perform_broadcast(is_emergency=False):
    try:
        with db_lock:
            own_ship_data = db_manager.get_own_ship_data()

        if own_ship_data and own_ship_data[2] is not None:
            _, nama, lat, lintang, lon, bujur, status, gps_date, gps_time = own_ship_data
            
            if is_emergency:
                status = 'DRT'

            data_paket = {
                "nama": nama, "lat": lat, "lintang": lintang, "lon": lon, "bujur": bujur,
                "status": status, "date": gps_date, "time": gps_time
            }
            
            pesan = json.dumps(data_paket).encode('utf-8')
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            try:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'sl0')
            except OSError as e:
                print(f"[SENDER] Gagal mengikat ke sl0 (mungkin bukan Linux atau tidak ada izin): {e}")

            broadcast_address = (config.BROADCAST_IP, config.UDP_PORT)
            sock.sendto(pesan, broadcast_address)
            print(f"[SENDER] Data dikirim ke broadcast: {data_paket}")

            if is_emergency:
                harbor_address = (config.HARBOR_IP, config.UDP_PORT)
                sock.sendto(pesan, harbor_address)
                print(f"[SENDER] Data darurat dikirim ke pelabuhan {config.HARBOR_IP}")
            
            sock.close()
        else:
            print("[SENDER] Gagal mengambil data diri dari DB atau posisi kosong.")

        try:
            with open(config.BEEP_CMD_FILE, 'w') as f:
                pass
            print("[SENDER] File 'beep.cmd' dibuat.")
        except IOError as e:
            print(f"[SENDER] Gagal membuat file beep: {e}")

    except Exception as e:
        print(f"[SENDER] Error dalam perform_broadcast: {e}")


def send_location_manager():
    print("[SENDER] Thread pengirim dimulai.")
    last_regular_broadcast_time = time.monotonic() - config.BROADCAST_INTERVAL_SECONDS + 10

    while True:
        if os.path.exists(config.EMERGENCY_CMD_FILE):
            print("[SENDER] File perintah darurat ditemukan!")
            perform_broadcast(is_emergency=True)
            try:
                os.remove(config.EMERGENCY_CMD_FILE)
                print("[SENDER] File perintah darurat dihapus.")
            except OSError as e:
                print(f"[SENDER] Gagal menghapus file perintah: {e}")
            last_regular_broadcast_time = time.monotonic()

        current_time = time.monotonic()
        if (current_time - last_regular_broadcast_time) >= config.BROADCAST_INTERVAL_SECONDS:
            print("[SENDER] Waktunya broadcast reguler...")
            perform_broadcast(is_emergency=False)
            last_regular_broadcast_time = current_time

        time.sleep(1)


def listen_for_locations():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', config.UDP_PORT)
    sock.bind(server_address)
    print(f"[LISTENER] Mendengarkan di port {config.UDP_PORT}.")

    while True:
        try:
            data, address = sock.recvfrom(1024)
            data_paket = json.loads(data.decode('utf-8'))
            print(f"[LISTENER] Menerima data dari {address}: {data_paket}")
            
            nama_kapal = data_paket.get("nama")
            
            if nama_kapal and nama_kapal != config.MY_SHIP_CODE:
                status = data_paket.get("status")
                
                if status and status.upper() == 'DRT':
                    print(f"[LISTENER] KONDISI DARURAT (DRT) TERDETEKSI DARI: {nama_kapal}")
                    if not os.path.exists(config.EMERGENCY_FLAG_FILE):
                        with open(config.EMERGENCY_FLAG_FILE, 'w') as f:
                            json.dump(data_paket, f)
                        print(f"[LISTENER] File interupsi '{config.EMERGENCY_FLAG_FILE}' telah dibuat.")
                
                lat = data_paket.get("lat"); lon = data_paket.get("lon")
                gps_date = data_paket.get("date"); gps_time = data_paket.get("time")

                lintang = data_paket.get("lintang")
                bujur = data_paket.get("bujur")

                if lat is not None and lon is not None:
                    with db_lock:
                        db_manager.update_or_insert_neighbor(
                            nama=nama_kapal, lat=lat, lintang=lintang, lon=lon,
                            bujur=bujur, status=status, gps_date=gps_date, gps_time=gps_time
                        )
                else:
                    print(f"[LISTENER] Data 'lat' atau 'lon' tidak ada dari {nama_kapal}.")
            else:
                print("[LISTENER] Data dari diri sendiri diabaikan.")
        except Exception as e:
            print(f"[LISTENER] Terjadi error: {e}")

if __name__ == "__main__":
    db_manager.setup_database()
    sender_thread = threading.Thread(target=send_location_manager, daemon=True)
    listener_thread = threading.Thread(target=listen_for_locations, daemon=True)
    sender_thread.start()
    listener_thread.start()
    print("Sistem Sharing Lokasi berjalan dengan 2 thread.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram sharing_lokasi.py dihentikan.")
