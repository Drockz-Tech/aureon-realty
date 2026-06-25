from PIL import Image

img = Image.open("logo-removebg-preview.png")
img = img.convert("RGBA")
width, height = img.size

# Find rows with non-transparent pixels
rows = []
for y in range(height):
    has_pixel = False
    for x in range(width):
        r, g, b, a = img.getpixel((x, y))
        if a > 10:
            has_pixel = True
            break
    if has_pixel:
        rows.append(y)

# Let's see the gaps between rows to identify the gap between the keys and the text
gaps = []
for i in range(1, len(rows)):
    if rows[i] - rows[i-1] > 5: # Gap larger than 5 pixels
        gaps.append((rows[i-1], rows[i]))

print(f"Image size: {width}x{height}")
print(f"Non-transparent rows: from {rows[0]} to {rows[-1]}")
print(f"Gaps found: {gaps}")
