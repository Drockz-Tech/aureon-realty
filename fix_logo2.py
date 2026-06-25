from PIL import Image

def remove_white_background(img_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Calculate how close the pixel is to white
        r, g, b, a = item
        
        # We assume the keys are golden (high R, high G, low B). 
        # White background is high R, high G, high B.
        # So if Blue is high, it's likely the background or anti-aliased edge.
        # Let's use a threshold.
        
        # If it's very bright gray/white
        if r > 180 and g > 180 and b > 180:
            # Scale alpha based on how close it is to white
            # If all are 255, alpha is 0. If all are 180, alpha is 255.
            avg = (r + g + b) / 3
            alpha = int(255 - ((avg - 180) / (255 - 180)) * 255)
            # Ensure we don't go out of bounds
            alpha = max(0, min(255, alpha))
            newData.append((r, g, b, alpha))
        elif r < 30 and g < 30 and b < 30:
            # Make dark/black artifacts transparent
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")

# Let's restore the original AI generated image first to not compound artifacts
import shutil
src_img = r"C:\Users\LENOVO\.gemini\antigravity-ide\brain\02025e57-03f7-456d-a1db-a87067c75a59\golden_keys_1782310901093.png"
dst_img = "golden_keys.png"
shutil.copy(src_img, dst_img)

remove_white_background("golden_keys.png")
