from PIL import Image

img = Image.open('561.png').convert('L') #8-bit grayscale 

raw = img.tobytes() # convert into bytes

n = 561

print(raw[:n].decode('utf-8')) # convert into utf-8