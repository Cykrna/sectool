from cryptography.fernet import Fernet
import json, os

KEY_FILE = "cykrna.key"
CONFIG_FILE = "config.json.enc"

def load_key():
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f:
            f.write(Fernet.generate_key())
    with open(KEY_FILE, "rb") as f:
        return f.read()

cipher = Fernet(load_key())

def save_config(data):
    encrypted = cipher.encrypt(json.dumps(data).encode())
    with open(CONFIG_FILE, "wb") as f:
        f.write(encrypted)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "rb") as f:
            decrypted = cipher.decrypt(f.read())
            return json.loads(decrypted.decode())
    return {}
