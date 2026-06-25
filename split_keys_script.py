from PIL import Image
import numpy as np

img = Image.open('keys_no_bg.png').convert('RGBA')
data = np.array(img)

h, w = data.shape[:2]
cx, cy = w // 2, h // 2

# We want to create key1 ( \ ) and key2 ( / )
data1 = data.copy()
data2 = data.copy()

# For key1 (\), we want to erase the top-right and bottom-left
# But keep a central circle intact so we don't break the overlap
radius = min(w, h) * 0.15

for y in range(h):
    for x in range(w):
        dx = x - cx
        dy = y - cy
        dist = np.sqrt(dx*dx + dy*dy)
        
        # Quadrants:
        # Top-Right: dx > 0, dy < 0
        # Bottom-Left: dx < 0, dy > 0
        if dist > radius:
            # Erase from key1 if in top-right or bottom-left
            if (dx > 0 and dy < 0) or (dx < 0 and dy > 0):
                # We can add a slight angle tolerance, but let's just wipe the quadrant
                # Actually, the keys are thick, so we might clip the edges if we wipe strictly by quadrant.
                # Let's check distance to the diagonal lines instead.
                pass

# Distance to diagonal method:
# Diagonal 1 (\): y = x * (h/w) => x*h - y*w = 0
# Diagonal 2 (/): y = -x * (h/w) + h => x*h + y*w - w*h = 0

for y in range(h):
    for x in range(w):
        # distance to diagonal 1 (\)
        dist1 = abs(x * h - y * w) / np.sqrt(h*h + w*w)
        # distance to diagonal 2 (/)
        dist2 = abs(x * h + y * w - w * h) / np.sqrt(h*h + w*w)
        
        dist_to_center = np.sqrt((x-cx)**2 + (y-cy)**2)
        
        if dist_to_center > radius:
            # If it's closer to diagonal 2 than diagonal 1, it belongs to key 2
            if dist2 < dist1:
                data1[y, x, 3] = 0 # Erase from key 1
            else:
                data2[y, x, 3] = 0 # Erase from key 2

Image.fromarray(data1).save('key1.png')
Image.fromarray(data2).save('key2.png')
print("Successfully split keys into key1.png and key2.png")
