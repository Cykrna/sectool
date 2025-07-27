import requests, os

HIBP_API_KEY = "YOUR_API_KEY"

def breach_menu():
    email = input("Enter email: ")
    r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                     headers={"hibp-api-key": HIBP_API_KEY, "user-agent": "CykrnaSuite"})
    if r.status_code == 200:
        print(r.json())
    else:
        print("No breaches found or error.")
    input("Press Enter...")
