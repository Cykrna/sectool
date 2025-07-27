from vpn import vpn_menu, get_vpn_status
from darkweb import darkweb_menu
from breach import breach_menu
import os

def main_menu():
    while True:
        os.system("clear")
        print("=== Cykrna Data Suite v4 ===")
        print(f"VPN Status: {get_vpn_status()}")
        print("""
1. My Data
2. OSINT Tools
3. Breach Check
4. Dark Web Monitor
5. VPN Control
6. Exit
""")
        choice = input("Select: ")
        if choice == "1":
            print("Visit: https://takeout.google.com or https://www.facebook.com/dyi")
            input("Press Enter...")
        elif choice == "2":
            print("Run PhoneInfoga or Shodan in separate module.")
            input("Press Enter...")
        elif choice == "3":
            breach_menu()
        elif choice == "4":
            darkweb_menu()
        elif choice == "5":
            vpn_menu()
        elif choice == "6":
            break
        else:
            input("Invalid choice! Press Enter...")

if __name__ == "__main__":
    main_menu()
