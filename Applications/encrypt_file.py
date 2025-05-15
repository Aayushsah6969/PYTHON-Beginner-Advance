from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from pathlib import Path
import secrets
import getpass

def encrypt_file(file_path: str, password: str):
    file = Path(file_path)
    if not file.exists() or not file.is_file():
        print("❌ Invalid file path.")
        return

    # Derive a 32-byte key from password
    key = password.encode("utf-8").ljust(32, b'\0')[:32]  # pad/truncate to 32 bytes
    aesgcm = AESGCM(key)

    nonce = secrets.token_bytes(12)
    data = file.read_bytes()
    encrypted = aesgcm.encrypt(nonce, data, None)

    encrypted_file = file.with_suffix(file.suffix + ".enc")
    with open(encrypted_file, "wb") as f:
        f.write(nonce + encrypted)

    print(f"✅ Encrypted: {file.name} → {encrypted_file.name}")
    file.unlink()
    print(f"🗑️ Deleted original: {file.name}")

if __name__ == "__main__":
    file_path = input("Enter full file path to lock: ").strip()
    password = getpass.getpass("Set password: ")
    encrypt_file(file_path, password)
