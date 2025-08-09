import os

print("run file")
notes_dir = os.path.expanduser("~/notes")

for filename in os.listdir(notes_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(notes_dir, filename)

        with open(filepath, "r") as file:
            lines = file.readlines()

        if "# Done" not in "".join(
            lines
        ):  # only edit files which have a "# Done" line. This line should be manually added by the user.
            continue

        remaining = []
        done_section = []
        crossed_out = []
        found_done = False

        # Separate crossed-out lines and remaining lines
        for line in lines:
            if "# Done" in line:
                found_done = True

            if found_done:
                done_section.append(line)
            elif line.lstrip().startswith("- [x]"):
                crossed_out.append(line)
            else:
                remaining.append(line)

        # If we found the "# Done" line and any crossed-out lines, update the file
        if found_done and crossed_out:
            with open(filepath, "w") as file:
                # Write the remaining lines (everything before "# Done")
                file.writelines(remaining)
                # Write the "# Done" section and append crossed-out lines to the end
                file.writelines(done_section)
                file.writelines(crossed_out)
