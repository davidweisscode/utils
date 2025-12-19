# This script is used to edit Obsidian markdown files in the user's notes directory.
# Crossed out tasks (lines starting with "- [x]") that appear before a line containing "# Done"
# are moved to the end of the file, after the "# Done" line. This helps in archiving completed tasks.
# The script is scheduled to run periodically using cron.

import os

print("start: move crossed out lines to archive at end of file")
notes_dir = os.path.expanduser("~/notes")  # assume Obsidian vault is at ~/notes

for filename in os.listdir(notes_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(notes_dir, filename)

        with open(filepath, "r") as file:
            lines = file.readlines()

        if (
            "# Archive" not in "".join(lines)
        ):  # only edit files which have an "# Archive" line. This line should be manually added by the user at the end of a note.
            continue

        remaining = []
        done_section = []
        crossed_out = []
        found_done = False

        # Separate crossed-out lines and remaining lines
        for line in lines:
            if "# Archive" in line:
                found_done = True

            if found_done:
                done_section.append(line)
            elif line.lstrip().startswith("- [x]"):
                crossed_out.append(line)
            else:
                remaining.append(line)

        # If we found the "# Archive" line and any crossed-out lines, update the file
        if found_done and crossed_out:
            with open(filepath, "w") as file:
                # Write the remaining lines (everything before "# Archive")
                file.writelines(remaining)
                # Write the "# Archive" section and append crossed-out lines to the end
                file.writelines(done_section)
                file.writelines(crossed_out)
