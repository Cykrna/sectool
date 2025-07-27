import os, json, requests, schedule, time, smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

DATA_FILE = "cykrna_data.json"
KEY_FILE = "cykrna_key.key"
ALERT_EMAIL = "youremail@example.com"  # Your email for alerts
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "youremail@example.com"
SMTP_PASS = "yourpassword"

# Generate key if not exists
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    key = f.read()
cipher = Fernet(key)

def save_data(label, data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            decrypted = cipher.decrypt(f.read())
            old_data = json.loads(decrypted.decode())
    else:
        old_data = {}
    old_data[label] = data
    encrypted = cipher.encrypt(json.dumps(old_data).encode())
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            decrypted = cipher.decrypt(f.read())
            return json.loads(decrypted.decode())
    return {}

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ALERT_EMAIL
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(SMTP_USER, ALERT_EMAIL, msg.as_string())
    server.quit()

def check_leaks_auto():
    stored_data = read_data()
    tracked_emails = [k.split("_")[1] for k in stored_data if k.startswith("Breach_")]
    for email in tracked_emails:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                         headers={"hibp-api-key":"YOUR_API_KEY","user-agent":"CykrnaSuite"})
        if r.status_code == 200:
            new_data = r.json()
            if stored_data.get(f"Breach_{email}") != new_data:
                save_data(f"Breach_{email}", new_data)
                send_alert("New Data Breach Detected!", f"{email} found in new breach: {new_data}")
                print(f"[ALERT] New breach detected for {email}")
        else:
            print(f"No new breaches for {email}")

def schedule_alerts():
    print("Dark Web Leak Alerts Enabled (24h check).")
    schedule.every(24).hours.do(check_leaks_auto)
    while True:
        schedule.run_pending()
        time.sleep(60)

def menu():
    os.system("clear")
    print("""
    =============================
      CYKRNA DATA SUITE (v2)
    =============================
    1. My Data (Google, Meta, Apple)
    2. OSINT Tools (PhoneInfoga, Shodan)
    3. Check Leaks (Manual)
    4. View Stored Results
    5. Enable Dark Web Leak Alerts
    6. Exit
    """)
    choice = input("Select an option: ")
    if choice == "1":
        my_data()
    elif choice == "2":
        osint_tools()
    elif choice == "3":
        breach_check()
    elif choice == "4":
        view_results()
    elif choice == "5":
        schedule_alerts()
    else:
        exit()

def my_data():
    print("""
    [1] Google Takeout: https://takeout.google.com
    [2] Facebook Data: https://www.facebook.com/dyi
    [3] Instagram Data: https://www.instagram.com/download/request
    [4] WhatsApp Data: Open app → Settings → Account → Request Info
    [5] Apple Data: https://privacy.apple.com
    [6] Microsoft Data: https://account.microsoft.com/privacy
    """)
    input("Press Enter to go back...")
    menu()

def osint_tools():
    print("""
    [1] PhoneInfoga (Phone Number Info)
    [2] Shodan (Public Device Search)
    """)
    ch = input("Select: ")
    if ch == "1":
        number = input("Enter phone number (e.g. +919876543210): ")
        result = {"number": number, "info": "Sample lookup (API key needed)"}
        save_data(f"PhoneInfo_{number}", result)
        print("Result saved securely.")
    elif ch == "2":
        query = input("Enter Shodan query: ")
        print(f"Open in browser: https://www.shodan.io/search?query={query}")
    input("Press Enter to go back...")
    menu()

def breach_check():
    email = input("Enter your email to check breaches: ")
    r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                     headers={"hibp-api-key":"YOUR_API_KEY","user-agent":"CykrnaSuite"})
    if r.status_code == 200:
        print("Breaches Found.")
        save_data(f"Breach_{email}", r.json())
    else:
        print("No breaches found or invalid email.")
    input("Press Enter to go back...")
    menu()

def view_results():
    data = read_data()
    print(json.dumps(data, indent=4))
    input("Press Enter to go back...")
    menu()

menu()
