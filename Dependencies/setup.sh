#!/bin/bash
echo "🔥 ShadowDaemon Ultimate Installer - イズミー"
echo "==============================================="

pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git nano wget curl -y
pkg install scrot fswebcam alsa-utils -y
pkg install nmap net-tools -y
pkg install openjdk-17 gradle -y
pkg install apktool -y

pip install -r requirements.txt

mkdir -p modules c2 kernel

echo "✅ Installation complete!"
echo "📝 Edit config.json with your credentials"
echo "🚀 Run: python3 shadow.py"