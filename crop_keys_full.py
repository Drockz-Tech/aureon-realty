from PIL import Image

img = Image.open("logo-removebg-preview.png")
width, height = img.size

min_y, max_y = 95, 265
min_x = width
max_x = 0

for y in range(min_y, max_y):
    for x in range(width):
        r, g, b, a = img.getpixel((x, y))
        if a > 10:
            if x < min_x: min_x = x
            if x > max_x: max_x = x

print(f"Keys bounding box X: {min_x} to {max_x}")

# Let's just crop it while we're at it!
cropped_img = img.crop((min_x, min_y, max_x, max_y))
cropped_img.save("golden_keys.png", "PNG")
print("Image tightly cropped on all sides and saved to golden_keys.png")
