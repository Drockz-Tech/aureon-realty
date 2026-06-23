from PIL import Image

try:
    img = Image.open('down.png')
    width, height = img.size
    print(f"Original size: {width}x{height}")
    
    # The skyline is at the bottom. Let's crop the bottom 25% of the image.
    # We will adjust this if needed, but usually the skyline is the bottom 20-30%.
    # Let's crop from height * 0.75 to height.
    crop_y = int(height * 0.70)
    cropped_img = img.crop((0, crop_y, width, height))
    cropped_img.save('skyline.png')
    print("Successfully cropped and saved skyline.png!")
except Exception as e:
    print(f"Error: {e}")
