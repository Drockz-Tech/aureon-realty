from PIL import Image

img = Image.open("golden_keys.png")
# Resize to multiple sizes for a proper icon file
icon_sizes = [(16,16), (32,32), (48,48), (64,64)]
img.save("favicon.ico", format="ICO", sizes=icon_sizes)
