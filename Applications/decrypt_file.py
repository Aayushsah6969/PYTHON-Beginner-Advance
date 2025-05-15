from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from pathlib import Path
import getpass

def decrypt_file(file_path: str, password: str):
    file = Path(file_path)
    if not file.exists() or not file.suffix.endswith(".enc"):
        print("❌ Invalid or non-encrypted file.")
        return

    key = password.encode("utf-8").ljust(32, b'\0')[:32]
    aesgcm = AESGCM(key)

    data = file.read_bytes()
    nonce = data[:12]
    encrypted = data[12:]

    try:
        decrypted = aesgcm.decrypt(nonce, encrypted, None)
        original_file = file.with_suffix('')  # remove .enc
        with open(original_file, "wb") as f:
            f.write(decrypted)
        print(f"✅ Decrypted: {file.name} → {original_file.name}")
        file.unlink()
        print(f"🗑️ Deleted encrypted file: {file.name}")
    except Exception as e:
        print(f"❌ Failed to decrypt: {e}")

if __name__ == "__main__":
    file_path = input("Enter full file path to unlock: ").strip()
    password = getpass.getpass("Enter password: ")
    decrypt_file(file_path, password)
