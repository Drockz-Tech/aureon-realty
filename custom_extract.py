from PIL import Image, ImageDraw

def remove_black_bg(img_path, out_path, tolerance=25):
    img = Image.open(img_path).convert("RGBA")
    
    # Floodfill from the corners to replace black background with transparent pixels
    ImageDraw.floodfill(img, (0, 0), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (img.width-1, 0), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (0, img.height-1), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (img.width-1, img.height-1), (0, 0, 0, 0), thresh=tolerance)
    
    # Also floodfill some midpoints on the edges just in case
    ImageDraw.floodfill(img, (img.width//2, 0), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (img.width//2, img.height-1), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (0, img.height//2), (0, 0, 0, 0), thresh=tolerance)
    ImageDraw.floodfill(img, (img.width-1, img.height//2), (0, 0, 0, 0), thresh=tolerance)

    img.save(out_path)

remove_black_bg("keys_only.jpg", "keys_no_bg.png", tolerance=35)
print("Done extracting using floodfill!")
