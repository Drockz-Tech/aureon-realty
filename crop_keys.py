from PIL import Image

img = Image.open("logo-removebg-preview.png")
# We will crop from x=0, y=0 to x=width, y=270
# This safely includes the keys (which end at y=257) and cuts off the text (which starts at y=281)
width, height = img.size
cropped_img = img.crop((0, 0, width, 270))

# Save over the old golden_keys.png
cropped_img.save("golden_keys.png", "PNG")
