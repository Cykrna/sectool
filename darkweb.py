import subprocess, os

def darkweb_menu():
    keyword = input("Enter email/phone/domain to search: ")
    print(f"[*] Searching dark web for {keyword}...")
    try:
        output = subprocess.check_output(["python3", "onionsearch/onionsearch.py", "-s", keyword], text=True)
        print(output)
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter...")
