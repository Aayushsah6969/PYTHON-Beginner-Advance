import zipfile
import os
from PIL import Image
from pathlib import Path

def zip_to_pdf(zip_path):
    zip_path = Path(zip_path)
    
    # Ensure the file exists and is a zip
    if not zip_path.exists() or zip_path.suffix.lower() != '.zip':
        print("Invalid ZIP file path.")
        return

    extract_dir = zip_path.with_name(zip_path.stem + "_extracted")

    # Extract the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    # Get all image files (sorted for proper order)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    image_files = sorted([f for f in extract_dir.iterdir() if f.suffix.lower() in image_extensions])

    if not image_files:
        print("No images found in the ZIP archive.")
        return

    # Open images using PIL
    images = [Image.open(img).convert('RGB') for img in image_files]

    # Output PDF file path
    pdf_path = zip_path.with_suffix('.pdf')

    # Save as PDF
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF saved to: {pdf_path}")

# Example usage
zip_to_pdf(r"C:\Users\KIIT0001\Desktop\AAYUSH\MY DOCUMENTS\college\materials\ch1.zip")

