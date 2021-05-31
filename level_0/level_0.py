#!/usr/bin/python3
"""
Requests a N numbers of times
"""
import requests

ID_user = "2814"
num_request = 1024
payload = {'id': ID_user, 'holdthedoor': 'Submit'}
URL = "http://158.69.76.135/level0.php"
errors = 0
request = 0
current_request = 0
print("Request to sent {}".format(num_request))

for index in range(current_request, num_request):
    r = requests.post(URL, data=payload)
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
