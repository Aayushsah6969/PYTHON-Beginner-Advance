import zipfile
import os
from PIL import Image
from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

lock = Lock()  # For thread-safe printing

def zip_to_pdf(zip_path: Path):
    extract_dir = zip_path.with_name(zip_path.stem + "_extracted")

    try:
        # Extract ZIP contents
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        # Find image files
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        image_files = sorted([f for f in extract_dir.iterdir() if f.suffix.lower() in image_extensions])

        if not image_files:
            with lock:
                print(f"⚠️ No images in {zip_path.name}. Skipping...")
            shutil.rmtree(extract_dir)
            return

        # Convert images to RGB and save as PDF
        images_iter = (Image.open(img).convert('RGB') for img in image_files)
        first_image = next(images_iter)

        pdf_path = zip_path.with_suffix('.pdf')
        first_image.save(pdf_path, save_all=True, append_images=list(images_iter))

        with lock:
            print(f"✅ Converted: {zip_path.name} → {pdf_path.name}")

    except Exception as e:
        with lock:
            print(f"❌ Failed: {zip_path.name} — {e}")

    finally:
        if extract_dir.exists():
            shutil.rmtree(extract_dir, ignore_errors=True)
        if zip_path.exists():
            zip_path.unlink()
        with lock:
            print(f"🧹 Cleaned: {zip_path.name}")

def convert_all_zips_in_directory(directory_path):
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        print("❌ Invalid directory path.")
        return

    zip_files = list(directory.glob("*.zip"))
    if not zip_files:
        print("📁 No ZIP files found in the directory.")
        return

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(zip_to_pdf, zip_files)

# === USAGE ===
# Replace with your ZIP folder path
convert_all_zips_in_directory(r"C:\path")