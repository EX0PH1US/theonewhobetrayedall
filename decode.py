from PIL import Image

img = Image.open('561.png').convert('L') # 8-bit grayscale 

raw = img.tobytes() # convert into bytes

n = 561 # length of the text message (even if you don't put it you will still be able to print the encoded text)


print(raw[:n].decode('utf-8')) # convert into utf-8

