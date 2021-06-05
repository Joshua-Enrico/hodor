#!/usr/bin/python3
import numpy as np
from PIL import Image
import pytesseract

im = Image.open('captcha.png')
data = np.array(im)

r1, g1, b1 = 0, 0, 0 # Original value
r2, g2, b2 = 128, 128, 128 # Value that we want to replace it with

red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
data[:,:,:3][mask] = [r2, g2, b2]

im = Image.fromarray(data)
im.save('fig1_modified.png')
captcha_pass = pytesseract.image_to_string("captcha.png", config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')
print(captcha_pass)
