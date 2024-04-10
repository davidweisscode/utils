import os
import re
import argparse


def get_new_name(filename):
    # Convert filename to lowercase
    new_name = filename.lower()

    # Replace spaces and underscores with dashes
    new_name = new_name.replace(" ", "-").replace("_", "-").replace(".jpeg", ".jpg")

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

    file_extension = filename.split(".")[-1]

    # Extract datetime string in the form of yyyymmdd-hhmmss using regex
    datetime_match = re.search(r"(\d{8}-\d{6})", new_name)
    if datetime_match:
        datetime_string = datetime_match.group(1)

        # Drop any characters after the match until the next dash
        datetime_parts = datetime_string.split("-")[:2]
        new_name = "-".join(datetime_parts)
        new_name += f".{file_extension}"

    return new_name


def rename_files(prod_mode=False):
    # Rename all files in the current directory
    print("[START] Rename files\n")

    for filename in os.listdir("."):
        if filename.endswith(".py"):
            continue
        new_name = get_new_name(filename)

        if prod_mode:
            # Rename the file in production mode
            print(f"{filename.ljust(30)} --> {new_name.ljust(30)} (Rename)")
            os.rename(filename, new_name)
        else:
            # Preview the renaming without actually renaming the files
            if filename == new_name:
                print(f"Same name: {new_name}")
            else:
                print(f"{filename.ljust(30)} --> {new_name.ljust(30)} (Preview)")

    print("\n[END] Rename files\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename image files")
    parser.add_argument(
        "--prod",
        action="store_true",
        help="Enable production mode (actual renaming)",
        default=False,
    )
    args = parser.parse_args()

    rename_files(prod_mode=args.prod)
