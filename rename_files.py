import os
import argparse


def get_new_name(filename):
    # Convert filename to lowercase
    new_name = filename.lower()

    # Replace spaces and underscores with dashes
    new_name = new_name.replace(" ", "-").replace("_", "-")

    # Remove specific substrings
    patterns_to_remove = [
        "pxl",
        "img",
        "whatsapp",
        "telegram",
        "image",
        "video",
        "photo",
        "screenshot",
        "night",
        "portrait",
        ".mp",
        "~",
    ]
    for pattern in patterns_to_remove:
        new_name = new_name.replace(pattern, "")

    # Remove leading and trailing dashes
    new_name = new_name.strip("-")

    return new_name


def rename_files(prod_mode=False):
    # Rename all files in the current directory
    print("[START] Rename files\n")

    for filename in os.listdir("."):
        new_name = get_new_name(filename)

        if prod_mode:
            # Rename the file in production mode
            os.rename(filename, new_name)
            print(f"Rename: '{filename}' --> '{new_name}'")
        else:
            # Preview the renaming without actually renaming the files
            print(f"Preview: '{filename}' --> '{new_name}'")

    print("\n[END] Rename files\n")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Rename image files")
    parser.add_argument(
        "--prod", action="store_true", help="Enable production mode (actual renaming)"
    )
    args = parser.parse_args()

    # Call rename_files function based on argument
    rename_files(prod_mode=args.prod)
