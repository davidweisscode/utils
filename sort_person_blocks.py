import re
import os


# Function to split the file into blocks
def split_blocks(content):
    blocks = []
    current_block = []

    for line in content:
        if line.startswith("# "):  # Indicates the start of a new person block
            if current_block:
                blocks.append(current_block)
            current_block = [line]  # Start a new block
        else:
            current_block.append(line)  # Add to the current block

    # Append the last block
    if current_block:
        blocks.append(current_block)

    return blocks


file_path = os.path.expanduser("~/notes/People.md")

# Read the input markdown file
with open(file_path, "r") as file:
    content = file.readlines()

# Split the content into person blocks
blocks = split_blocks(content)

# Sort blocks alphabetically by the person's name (the first line of each block)
sorted_blocks = sorted(blocks, key=lambda block: block[0].strip("# ").strip())

# Flatten the sorted blocks back into lines
sorted_content = []
for block in sorted_blocks:
    sorted_content.extend(block)

# Write the sorted content into a new markdown file
with open(file_path, "w") as file:
    file.writelines(sorted_content)
