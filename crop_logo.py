from PIL import Image

try:
    img = Image.open('down.png')
    width, height = img.size
    
    # The logo is at the top of the poster.
    # Let's crop the top 35% of the image to get JUST the ornate keys and maybe the "Aureon Realty LLC" text.
    # We want JUST the keys if possible. 
    # Let's crop the top 20% to get just the keys.
    crop_h = int(height * 0.25)
    
    logo_img = img.crop((0, 0, width, crop_h))
    logo_img.save('clean_logo.png')
    print("Successfully cropped logo to clean_logo.png!")
except Exception as e:
    print(f"Error: {e}")
