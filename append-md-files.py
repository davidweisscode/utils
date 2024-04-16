import os


def append_md_files_to_specific_file(folder_path, output_file_path):
    with open(output_file_path, "a", encoding="utf-8") as output_file:
        for filename in os.listdir(folder_path):
            if filename.endswith(".md"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r", encoding="utf-8") as md_file:
                    output_file.write(md_file.read())
                    output_file.write("\n")  # Add a newline after each file's content


folder_path = "/Users/A117803967/dev/rezepte"
output_file_path = "/Users/A117803967/notes/Recipes.md"

append_md_files_to_specific_file(folder_path, output_file_path)
