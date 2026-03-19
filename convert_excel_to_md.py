"""
convert_excel_to_md.py
Read an Excel sheet and write it as a GitHub‑flavoured
Markdown table.

Usage:
    python convert_excel_to_md.py input.xlsx output.md "Sheet1"
"""

import sys
import pandas as pd

# --- arguments -------------------------------------------------------------
input_xlsx = sys.argv[1]  # e.g. "data.xlsx"
output_md = sys.argv[2]  # e.g. "table.md"
sheet_name = sys.argv[3] if len(sys.argv) > 3 else 0  # name or index
# ---------------------------------------------------------------------------

# 1️⃣  read the sheet
df = pd.read_excel(input_xlsx, sheet_name=sheet_name)

# 2️⃣  convert to Markdown (needs `tabulate` under the hood)
markdown_table = df.to_markdown(index=False)

# 3️⃣  write to file
with open(output_md, "w", encoding="utf-8") as f:
    f.write(markdown_table + "\n")  # add newline for POSIX hygiene

print(f"✔️  Markdown table written to {output_md}")
