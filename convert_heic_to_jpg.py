import os
from PIL import Image
import pyheif

# Directory containing the images
directory = '/mnt/c/Users/David/Desktop/2024 Dolomites'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith('.heic'):
        # Full path to the HEIC file
        heic_file_path = os.path.join(directory, filename)
        
        # Read and convert the HEIC file
        heif_file = pyheif.read(heic_file_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Change the extension from .HEIC to .JPG
        jpg_file_path = os.path.splitext(heic_file_path)[0] + '.jpg'
        
        # Save the image as a JPG file
        image.save(jpg_file_path, "JPEG")
        
        print(f"Converted {filename} to {os.path.basename(jpg_file_path)}")
