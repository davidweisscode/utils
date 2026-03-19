import re

# Read your file
with open("bookmarks.html", "r", encoding="utf-8") as f:
    text = f.read()

# Pattern: HREF="(link)" ... > (title) </A>
pattern = re.compile(r'HREF="([^"]+)"[^>]*>(.*?)</A>', re.IGNORECASE)

for match in pattern.finditer(text):
    link = match.group(1)
    title = match.group(2)
    print(f"- {title}; {link}")
