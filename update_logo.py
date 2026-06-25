import re
import shutil

# Copy the generated golden keys image
src_img = r"C:\Users\LENOVO\.gemini\antigravity-ide\brain\02025e57-03f7-456d-a1db-a87067c75a59\golden_keys_1782310901093.png"
dst_img = "golden_keys.png"
shutil.copy(src_img, dst_img)

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the logo specifically in the s4-merge block (slide 4)
# We can use regex to find s4-merge and replace the img inside it
pattern = r'(<div class="s4-merge" id="s4-merge">\s*)<img src="logo-removebg-preview\.png"[^>]*>'
replacement = r'\1<img src="golden_keys.png" class="s4-logo-img" alt="Golden Keys" style="max-width: 150px; height: auto;">'

content = re.sub(pattern, replacement, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
