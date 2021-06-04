#!/usr/bin/python3
"""
Requests a N numbers of times
"""

import requests
from bs4 import BeautifulSoup
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

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
    captcha_img = open("captcha.png", "wb")
    captcha_img.write(captcha.content)
    captcha_img.close()
    captcha_pass = pytesseract.image_to_string("captcha.png", config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

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
