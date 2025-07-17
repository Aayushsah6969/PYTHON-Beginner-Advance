import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# 🔐 Input password
pwd = input("Enter password to set for all PDFs: ")
base_dir = Path("/home/blackperl/Downloads/desifakes.com")  # Set your folder
lock = Lock()

def lock_pdf(pdf_path: Path):
    try:
        # Quick pre-check for corruption
        with open(pdf_path, "rb") as f:
            if f.read(4) != b'%PDF':
                with lock:
                    print(f"⚠️ Not a valid PDF header: {pdf_path.name}")
                return

        reader = PdfReader(pdf_path, strict=False)

        # Skip already locked
        if reader.is_encrypted:
            with lock:
                print(f"⏭️ Skipped (Already Locked): {pdf_path.name}")
            return

        writer = PdfWriter()

        # Add pages
        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(pwd)

        temp_path = pdf_path.with_suffix(".locked.pdf")
        with open(temp_path, "wb") as f:
            writer.write(f)

        temp_path.replace(pdf_path)  # Overwrite only after success

        with lock:
            print(f"🔐 Locked: {pdf_path.name}")

    except Exception as e:
        with lock:
            print(f"❌ Failed: {pdf_path.name} — {e}")

def lock_all_pdfs_in_directory(directory: Path, max_workers=4):
    if not directory.exists() or not directory.is_dir():
        print("❌ Invalid directory path.")
        return

    pdf_files = list(directory.rglob("*.pdf"))
    if not pdf_files:
        print("📁 No PDF files found.")
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(lock_pdf, path) for path in pdf_files]
        for _ in as_completed(futures):
            pass  # All output is handled inside lock_pdf

# === RUN ===
lock_all_pdfs_in_directory(base_dir, max_workers=4)
