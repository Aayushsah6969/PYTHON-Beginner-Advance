import zipfile
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import img2pdf  # Install via pip if missing: pip install img2pdf

lock = Lock()  # For thread-safe prints

def zip_to_pdf(zip_path: Path, keep_zip=False):
    extract_dir = zip_path.with_name(zip_path.stem + "_extracted")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        # Supported image extensions
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

        # Get sorted list of image file paths
        image_files = sorted(
            [f for f in extract_dir.iterdir() if f.suffix.lower() in image_extensions]
        )

        if not image_files:
            with lock:
                print(f"⚠️ No images found in {zip_path.name}. Skipping...")
            return

        # Validate images by trying to open (skip broken images)
        valid_images = []
        for img_path in image_files:
            try:
                # Just check if file is readable by img2pdf (open in binary mode)
                with open(img_path, "rb") as f:
                    if f.read(4):  # quick read to confirm file is not empty
                        valid_images.append(str(img_path))
            except Exception:
                with lock:
                    print(f"⚠️ Skipping unreadable image: {img_path.name}")

        if not valid_images:
            with lock:
                print(f"⚠️ No valid images to convert in {zip_path.name}. Skipping...")
            return

        pdf_path = zip_path.with_suffix('.pdf')

        # Convert images to PDF efficiently using img2pdf (low memory)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(valid_images))

        with lock:
            print(f"✅ Converted: {zip_path.name} → {pdf_path.name}")

    except Exception as e:
        with lock:
            print(f"❌ Failed: {zip_path.name} — {e}")

    finally:
        # Clean up extracted images folder
        if extract_dir.exists():
            shutil.rmtree(extract_dir, ignore_errors=True)

        # Delete original ZIP unless user wants to keep it
        if zip_path.exists() and not keep_zip:
            zip_path.unlink()

        with lock:
            print(f"🧹 Cleaned up: {zip_path.name}")


def convert_all_zips_in_directory(directory_path, max_workers=4, keep_zip=False):
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        print("❌ Invalid directory path.")
        return

    zip_files = list(directory.glob("*.zip"))
    if not zip_files:
        print("📁 No ZIP files found in the directory.")
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(zip_to_pdf, zip_path, keep_zip) for zip_path in zip_files]

        # Optional: wait for all to complete with progress print
        for future in as_completed(futures):
            # Exceptions are already caught inside zip_to_pdf
            pass


# === USAGE ===
# Set your directory here, reduce max_workers to lower CPU & RAM usage
convert_all_zips_in_directory("/home/blackperl/Downloads/desifakes.com", max_workers=4, keep_zip=False)
