from rembg import remove
from PIL import Image

input_path = 'keys_only.jpg'
output_path = 'keys_no_bg.png'

print("Opening image...")
input_img = Image.open(input_path)
print("Removing background...")
output_img = remove(input_img)
print("Saving image...")
output_img.save(output_path)
print("Done!")
