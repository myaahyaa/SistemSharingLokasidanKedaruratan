# math_utils.py

from math import radians, sin, cos, acos, atan2, degrees

def calculate_distance(lat1, lon1, lat2, lon2):
    """Menghitung jarak antara dua titik koordinat menggunakan rumus Haversine (dalam km)."""
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return None

    # Konversi derajat ke radian
    rad_lat1 = radians(lat1)
    rad_lon1 = radians(lon1)
    rad_lat2 = radians(lat2)
    rad_lon2 = radians(lon2)

    # Radius bumi dalam kilometer
    R = 6371.0

    dlon = rad_lon2 - rad_lon1
    dlat = rad_lat2 - rad_lat1

    # Rumus Haversine
    a = sin(dlat / 2)**2 + cos(rad_lat1) * cos(rad_lat2) * sin(dlon / 2)**2
    c = 2 * atan2(a**0.5, (1 - a)**0.5)
    distance = R * c
    
    return distance

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Menghitung arah/bearing awal dari titik 1 ke titik 2 (dalam derajat)."""
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return None
        
    rad_lat1 = radians(lat1)
    rad_lon1 = radians(lon1)
    rad_lat2 = radians(lat2)
    rad_lon2 = radians(lon2)

    dLon = rad_lon2 - rad_lon1

    # Rumus Bearing
    y = sin(dLon) * cos(rad_lat2)
    x = cos(rad_lat1) * sin(rad_lat2) - sin(rad_lat1) * cos(rad_lat2) * cos(dLon)
    
    bearing_rad = atan2(y, x)
    bearing_deg = (degrees(bearing_rad) + 360) % 360 # Konversi ke 0-360 derajat
    
    return bearing_deg
