from PIL import Image

def remove_background():
    img = Image.open("logo.png").convert("RGBA")
    pixels = img.load()

    # Get the background color from the top-left corner
    bg_color = pixels[0, 0]

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            
            # Calculate distance from the background color
            dist = ((bg_color[0] - r)**2 + (bg_color[1] - g)**2 + (bg_color[2] - b)**2)**0.5
            
            # If it's the background color (or very close), make it fully transparent
            if dist < 60:
                pixels[x, y] = (255, 255, 255, 0)
            else:
                # Keep the logo pixels fully opaque (fixes the "hiding" issue)
                pixels[x, y] = (r, g, b, 255)

    # Crop the image to strictly the name and symbol (removes the square container)
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    img.save("logo_transparent2.png")
    print("Successfully removed background and cropped to symbol/name.")

if __name__ == "__main__":
    remove_background()
