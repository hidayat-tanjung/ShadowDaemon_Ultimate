#!/bin/bash
echo "🔥 ShadowDaemon Ultimate Installer - イズミー"
pkg update -y && pkg upgrade -y
pkg install python git nano wget curl scrot fswebcam alsa-utils nmap net-tools -y
pip install -r requirements.txt
echo "✅ Done! Edit config.json then run: python3 shadow.py"
