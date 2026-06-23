from PIL import Image

img = Image.open("logo.png").convert("RGBA")
pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        # Distance from pure white
        dist = ((255 - r)**2 + (255 - g)**2 + (255 - b)**2)**0.5
        
        if dist < 80:
            # Scale alpha based on distance to white to preserve some anti-aliasing smoothly
            alpha = int((dist / 80) * 255)
            pixels[x, y] = (r, g, b, alpha)

img.save("logo_transparent.png")
print("Background removed and saved to logo_transparent.png")
