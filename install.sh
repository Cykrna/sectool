#!/bin/bash
echo "[*] Installing Cykrna Data Suite v4..."
pkg update -y
pkg install python git tor termux-api openvpn wireguard-tools -y
pip install requests cryptography schedule stem
git clone https://github.com/danielgatis/onionsearch
echo "[*] Installation complete!"
echo "Run with: python main.py"
