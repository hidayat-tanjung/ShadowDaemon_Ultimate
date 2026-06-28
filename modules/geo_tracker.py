import requests
import subprocess

def get_location():
    try:
        ip = subprocess.check_output("curl -s ifconfig.me", shell=True).decode().strip()
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        
        info = f"""
📍 GEOLOCATION:
IP: {data.get('ip')}
City: {data.get('city')}
Region: {data.get('region')}
Country: {data.get('country_name')}
Timezone: {data.get('timezone')}
ISP: {data.get('org')}
Lat: {data.get('latitude')}
Lon: {data.get('longitude')}
"""
        return info
    except:
        return "Geolocation failed"