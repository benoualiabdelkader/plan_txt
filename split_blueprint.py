import os
import re

file_path = "system_blueprint (1).txt"
output_dir = "."

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split by the section delimiter
pattern = r'(──────────────────────────────────────────\nOUTPUT SECTION .*)'
sections_raw = re.split(pattern, content)

# sections_raw will have:
# [0]: content before first match
# [1]: first delimiter match (e.g. "──────────────────────────────────────────\nOUTPUT SECTION 000 — IDEAL...")
# [2]: content after first match
# [3]: second delimiter match
# [4]: content after second match
# ...

if sections_raw[0].strip():
    with open("00_Header.txt", "w", encoding="utf-8") as f:
        f.write(sections_raw[0].strip())

for i in range(1, len(sections_raw), 2):
    header_line = sections_raw[i]
    body = sections_raw[i+1]
    
    # Extract the name from the header_line
    # e.g., "──────────────────────────────────────────\nOUTPUT SECTION 000 — IDEAL OPERATIONAL WORKFLOW (EXECUTIVE SUMMARY)"
    section_name = header_line.split("OUTPUT SECTION ")[1].strip()
    
    # Clean the name to make it a valid filename
    safe_name = "".join([c if c.isalnum() or c in " -_()" else "_" for c in section_name])
    # limit length to avoid too long file names
    safe_name = safe_name[:100]
    
    file_name = f"Section_{safe_name}.txt"
    file_path_out = os.path.join(output_dir, file_name)
    
    with open(file_path_out, "w", encoding="utf-8") as f:
        f.write(header_line + body)

print("Splitting complete.")
