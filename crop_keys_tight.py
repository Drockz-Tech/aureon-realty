from PIL import Image

# Re-open the original logo
img = Image.open("logo-removebg-preview.png")

# We crop tightly around the keys. 
# Previously found: non-transparent pixels for keys are from y=100 to y=257.
# We'll use y=95 to y=265 to be perfectly safe with soft edges.
width, height = img.size
cropped_img = img.crop((0, 95, width, 265))

# Save over golden_keys.png
cropped_img.save("golden_keys.png", "PNG")
