import os

def install_phoneinfoga():
    if not os.path.exists("phoneinfoga"):
        os.system("git clone https://github.com/sundowndev/phoneinfoga")
        os.system("cd phoneinfoga && pip install -r requirements.txt")
        print("PhoneInfoga installed.")

def phoneinfoga_menu():
    install_phoneinfoga()
    phone = input("Enter phone number (with country code): ")
    os.system(f"cd phoneinfoga && python3 phoneinfoga.py scan -n {phone}")
    input("Press Enter...")
