# Cykrna Data Suite v4

> **Disclaimer:**  
> This tool is created **strictly for educational and ethical purposes**.  
> It must **not** be used for any illegal activity, unauthorized access, or malicious intent.  
> The developer(s) of this project **do not take responsibility** for any misuse.

---

## **Features**
- **Menu-based interface** (fast & simple for Termux)
- **Dark Web Monitor** – Search `.onion` and paste sites for emails, phone numbers, or domains
- **Breach Check** – Uses HaveIBeenPwned API to check compromised accounts
- **VPN Control** –  
  - OpenVPN & WireGuard support  
  - Quick ProtonVPN setup for free servers  
  - Auto-connect before dark web scans
- **Automatic AES Encryption** – VPN credentials & configs are stored securely

---

## **Installation**
1. Open Termux and run:
   pkg update -y && pkg install git -y
   git clone https://github.com/Cykrna/sectool.git
   cd cykrna_suite
   chmod +x install_cykrna.sh
   ./install_cykrna.sh

#2. Start the tool:

cd cykrnasuit
chmod +x install.sh
./install.sh
python main.py




---

Usage

Main Menu

=== Cykrna Data Suite v4 ===
VPN Status: Connected/Disconnected

1. Breach Check
2. Dark Web Monitor
3. VPN Control
4. Exit

Breach Check: Enter an email → check against known data breaches.

Dark Web Monitor: Search onion sites for leaked data.

VPN Control: Import configs, connect/disconnect VPN, set up ProtonVPN.



---

#Configuration & Security

Encryption:

A random AES key (cykrna.key) is generated on first run.

All configs & credentials are stored in config.json.enc.


#Files:

cykrna.key – Encryption key (keep it safe).

config.json.enc – Encrypted settings.




---

#Dependencies

Python 3

Termux API

Tor

OpenVPN / WireGuard

Python modules:

pip install requests cryptography schedule stem



---

#Notes

Get a free API key from HaveIBeenPwned and put it in breach.py.

ProtonVPN users can create free accounts here.



---

Developed by: Cykrna Technologies

---

Would you like me to **make this a ready-to-use `.zip` package** (with README + scripts + installer), so you just extract and run?  
Or keep it as **separate scripts** for manual setup?  

Which do you want? **1. ZIP package** or **2. Separate files?**
