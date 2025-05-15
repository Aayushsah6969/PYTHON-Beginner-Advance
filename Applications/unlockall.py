import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

pwd = input("Enter password to unlock all PDFs: ")
base_dir = Path("parent")  # Change this to your parent folder path
lock = Lock()

def unlock_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        if not reader.is_encrypted:
            with lock:
                print(f"🔓 Already unlocked: {pdf_path}")
            return

        reader.decrypt(pwd)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(pdf_path, "wb") as f:
            writer.write(f)

        with lock:
            print(f"✅ Unlocked: {pdf_path}")
    except Exception as e:
        with lock:
            print(f"❌ Failed: {pdf_path} — {e}")

if __name__ == "__main__":
    pdf_files = list(Path(base_dir).rglob("*.pdf"))

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(unlock_pdf, pdf_files)
