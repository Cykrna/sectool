import os, subprocess

VPN_CONFIG = "/data/data/com.termux/files/home/cykrna_vpn.conf"

def get_vpn_status():
    result = os.popen("pgrep openvpn").read().strip()
    return "Connected" if result else "Disconnected"

def connect_openvpn():
    if os.path.exists(VPN_CONFIG):
        os.system(f"openvpn --config {VPN_CONFIG} &")
        input("Connecting... Press Enter.")
    else:
        input("No VPN config found. Import first.")

def disconnect_vpn():
    os.system("pkill openvpn")
    input("VPN disconnected. Press Enter.")

def import_vpn():
    path = input("Enter path to .ovpn file: ")
    if os.path.exists(path):
        os.system(f"cp {path} {VPN_CONFIG}")
        input("Config imported.")
    else:
        input("File not found.")

def protonvpn_setup():
    user = input("Enter ProtonVPN username: ")
    passwd = input("Enter ProtonVPN password: ")
    with open(VPN_CONFIG, "w") as f:
        f.write(f"auth-user-pass\nremote protonvpn.com\nproto udp\nport 1194\n")
    os.system("echo -e '{}\n{}' > /etc/openvpn/auth.txt".format(user, passwd))
    input("ProtonVPN setup done.")

def vpn_menu():
    while True:
        os.system("clear")
        print(f"=== VPN Menu ===\nStatus: {get_vpn_status()}\n")
        print("1. Connect VPN\n2. Disconnect VPN\n3. Import Config\n4. Setup ProtonVPN\n5. Back")
        choice = input("Select: ")
        if choice == "1":
            connect_openvpn()
        elif choice == "2":
            disconnect_vpn()
        elif choice == "3":
            import_vpn()
        elif choice == "4":
            protonvpn_setup()
        elif choice == "5":
            break
