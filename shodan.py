import requests
from utils import load_config, save_config

def shodan_menu():
    config = load_config()
    api_key = config.get("shodan_api")
    if not api_key:
        api_key = input("sA0aawA2vszTgx82M3mJKFPsCxTyYURQ: ")
        config["shodan_api"] = api_key
        save_config(config)

    query = input("Enter Shodan search query (IP/domain/service): ")
    url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={query}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            results = r.json()
            for match in results.get("matches", []):
                print(f"IP: {match.get('ip_str')}, Org: {match.get('org')}, Data: {match.get('data')[:100]}")
        else:
            print("Error:", r.text)
    except Exception as e:
        print("Error:", e)
    input("Press Enter...")
