from PIL import Image
import os

img_path = r"C:\Users\LENOVO\.gemini\antigravity-ide\brain\d007c569-a6b1-4551-98ea-8588b51b3f71\media__1782426890982.jpg"
img = Image.open(img_path)
width, height = img.size

# Crop the top ~72% of the image which contains the keys and keyhole, but not the text.
cropped_img = img.crop((0, 0, width, int(height * 0.72)))

out_path = r"c:\Users\LENOVO\OneDrive\Desktop\projects\gaurav\keys_only.jpg"
cropped_img.save(out_path, "JPEG", quality=95)
print(f"Saved cropped image to {out_path} (size: {width}x{int(height * 0.72)})")
