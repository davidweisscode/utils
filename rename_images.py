import os
import re
import sys
from typing import Optional


def get_new_name(file_name: str) -> str:
    # Convert file_name to lowercase
    new_file_name = file_name.lower()

    # Extract the file extension
    file_extension = new_file_name.split(".")[-1]

    # Rename for consistent .jpg file extension
    file_extension = file_extension.replace("jpeg", "jpg")

    # Extract the file name
    new_file_name = new_file_name.split(".")[0]

    # Remove specific substrings
    patterns_to_remove = [
        "pxl", "img", "whatsapp", "telegram", "image", "video",
        "photo", "screenshot", "night", "portrait", ".mp", "~"
    ]
    for pattern in patterns_to_remove:
        new_file_name = new_file_name.replace(pattern, "")

    # Replace spaces and underscores with dashes
    new_file_name = new_file_name.replace(" ", "-").replace("_", "-")

    # Remove leading and trailing dashes
    new_file_name = new_file_name.strip("-")

    # Extract datetime string in the form of yyyymmdd-hhmmss using regex
    datetime_match = re.search(r"(\d{8}-\d{6})", new_file_name)
    if datetime_match:
        datetime_string = datetime_match.group(1)

        # Drop any characters after the match until the next dash
        new_file_name = datetime_string
        new_file_name += f".{file_extension}"
    else:
        # If no datetime string is found, use the original new_file_name with the correct extension
        new_file_name += f".{file_extension}"

    return new_file_name



def main(dir_path: str, prod_mode: Optional[bool] = False) -> None:
    # Ensure the provided directory path is absolute
    if not os.path.isabs(dir_path):
        print("Please provide an absolute path to the directory.")
        return

    # Check if the provided path is a directory
    if not os.path.isdir(dir_path):
        print("The provided path is not a directory.")
        return
    
    print(f"\n[Start] Rename images: {dir_path}\n")
    
    # Get a list of file names in the directory
    file_names = os.listdir(dir_path)
    
    for file_name in file_names:
        # Construct the full file path
        file_path = os.path.join(dir_path, file_name)
        
        # Check if it's a file (not a dir_path)
        if os.path.isfile(file_path):
            # Construct the new file name
            # file_extension = os.path.splitext(file_name)[1]  # Get the file extension
            new_file_name = get_new_name(file_name)
            new_file_path = os.path.join(dir_path, new_file_name)

            if prod_mode:
                # Rename the file
                print(f"{file_name.ljust(35)} --> {new_file_name.ljust(30)} (Rename)")
                os.rename(file_path, new_file_path)
            else:
                # Print the new file name (dry run)
                print(f"{file_name.ljust(35)} --> {new_file_name.ljust(30)} (Preview)")

    print("\n[END] Rename images\n")


if __name__ == "__main__":
    # Check if the directory path or prod flag is provided as command line arguments
    if len(sys.argv) not in [2, 3]:
        print("Usage: python3 rename_images.py /absolute/path/to/dir/with/images/ [--prod]")
        sys.exit(1)

    # Get the directory path from the command line arguments
    dir_path = sys.argv[1]
    prod_mode = "--prod" in sys.argv

    # Call the main function
    main(dir_path, prod_mode)
