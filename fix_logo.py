from PIL import Image

def make_transparent(img_path):
    img = Image.open(img_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # If the pixel is mostly white (e.g. > 240 for R, G, B)
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0)) # Transparent
        elif item[0] < 15 and item[1] < 15 and item[2] < 15:
            # Also make black transparent just in case
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")

make_transparent("golden_keys.png")

# Now update the HTML to remove the filter
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the img tag for golden keys to ensure filter: none is applied
import re
pattern = r'<img src="golden_keys.png" class="s4-logo-img" alt="Golden Keys" style="max-width: 150px; height: auto;">'
replacement = r'<img src="golden_keys.png" class="s4-logo-img" alt="Golden Keys" style="max-width: 150px; height: auto; filter: none;">'

content = re.sub(pattern, replacement, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
