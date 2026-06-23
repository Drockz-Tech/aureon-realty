from PIL import Image
try:
    img = Image.open('Print.eps')
    # Render at high resolution
    img.load(scale=10)
    # Save as PNG
    img.save('Print_logo.png')
    print('EPS to PNG successful!')
except Exception as e:
    print('Failed:', str(e))
