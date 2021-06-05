#!/usr/bin/python3
"""
Requests a N numbers of times
"""

import requests
from bs4 import BeautifulSoup
import os

from PIL import Image

import numpy as np
import pytesseract
import cv2

ID_user = "2814"
num_request = 1024
errors = 0
request = 0
captcha_url = "http://158.69.76.135/tim.php"
ip = 'http://158.69.76.135/level5.php'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
current_request = 0
Cookies = 0
URL = "http://158.69.76.135/level5.php"
header = {
    "Content-Type": 'application/x-www-form-urlencoded',
    "user-Agent": user_agent,
    "referer": URL
}
payload = {
            'id': ID_user,
            'holdthedoor': 'Submit',
            'key': '',
            'captcha': ''
            }
for index in range(num_request):
    session = requests.session()
    page = session.get(URL, headers=header, cookies=Cookies)

    soup = BeautifulSoup(page.text, "html.parser")
    hidden_value = soup.find("form")
    hidden_value = hidden_value.find("input", {"type": "hidden"})
    hidden_value = hidden_value["value"]
    payload["key"] = hidden_value    

    Cookies = page.cookies

    captcha = session.get(captcha_url, headers=header)
    captcha_img = open("1.png", "wb")
    captcha_img.write(captcha.content)

    im = Image.open('1.png')
    data = np.array(im)
    
    r1, g1, b1 = 0, 0, 0 # Original value
    r2, g2, b2 = 128, 128, 128 # Value that we want to replace it with
    
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]
    
    im = Image.fromarray(data)
    im.save('3.png')


    captcha_pass = pytesseract.image_to_string("3.png", config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    
    new_captcha = ""
    br = 0
    for i in captcha_pass:
        new_captcha += i
        br += 1
        if br == 8:
            break
    print(new_captcha)
    payload["captcha"] = new_captcha



    r = session.post(URL, headers=header, data=payload, cookies=Cookies)
    if r.status_code == 200:
        print("Request accepted {}".format(request), end='\r')
        request += 1
    if r.status_code != 200:
        print("failed request number {}".format(errors), end='\r')
        errors += 1

print()
print()
print("Resume:")
print("Total requests {}".format(index + 1))
print("succesful requests {}".format(request))
print("failed requests {}".format(errors))
