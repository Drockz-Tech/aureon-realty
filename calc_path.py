import math

path_d = """
M 50 198 L 50 140 L 80 140 L 80 198 
M 100 198 L 100 100 L 140 100 L 140 198 
M 160 198 L 160 80 L 170 70 L 180 80 L 180 198 
M 220 198 L 220 120 L 270 120 L 270 198 
M 300 198 L 300 80 Q 340 100 380 198 
M 420 198 L 420 130 L 450 130 L 450 198 
M 470 198 L 470 150 L 485 150 L 485 80 L 495 80 L 495 20 L 500 0 L 505 20 L 505 80 L 515 80 L 515 150 L 530 150 L 530 198 
M 560 198 L 560 110 L 600 110 L 600 198 
M 630 198 L 630 60 L 650 60 L 650 198 
M 680 198 L 680 120 L 740 120 L 740 198 
M 780 198 L 780 90 L 820 90 L 820 198 
M 850 198 L 850 140 L 880 140 L 880 198 
M 920 198 L 920 160 L 960 160 L 960 198
"""

import re
commands = re.findall(r'([MLQ])\s+([0-9\.\s]+)', path_d)

total_length = 0
curr_x, curr_y = 0, 0

def dist(x1, y1, x2, y2):
    return math.hypot(x2-x1, y2-y1)

for cmd, coords_str in commands:
    coords = list(map(float, coords_str.strip().split()))
    if cmd == 'M':
        curr_x, curr_y = coords[0], coords[1]
    elif cmd == 'L':
        total_length += dist(curr_x, curr_y, coords[0], coords[1])
        curr_x, curr_y = coords[0], coords[1]
    elif cmd == 'Q':
        # approximate quadratic bezier with line segments
        cx, cy, ex, ey = coords
        steps = 10
        for i in range(1, steps + 1):
            t = i / steps
            nx = (1-t)**2 * curr_x + 2*(1-t)*t * cx + t**2 * ex
            ny = (1-t)**2 * curr_y + 2*(1-t)*t * cy + t**2 * ey
            total_length += dist(curr_x, curr_y, nx, ny)
            curr_x, curr_y = nx, ny

print(f"Total building path length: {total_length}")
