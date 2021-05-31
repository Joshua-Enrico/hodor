#!/usr/bin/python3
"""
Requests a N numbers of times
"""
import requests
from bs4 import BeautifulSoup

ID_user = "2814"
num_request = 4096
errors = 0
request = 0
current_request = 0
URL = "http://158.69.76.135/level1.php"

payload = {
            'id': ID_user,
            'holdthedoor': 'Submit',
            'key': ''
            }
for index in range(num_request):
    session = requests.session()
    page = session.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")
    hidden_value = soup.find("form")
    hidden_value = hidden_value.find("input", {"type": "hidden"})
    hidden_value = hidden_value["value"]
    payload["key"] = hidden_value

    r = session.post(URL, payload)
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
