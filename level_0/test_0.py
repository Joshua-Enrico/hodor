#!/usr/bin/python3
"""
Requests a N numbers of times
"""
import requests
try:
    ID_user = int(input("Enter id:"))
except Exception as Error:
    raise TypeError ("Only numbers Permited")

try:
num_requests = int(input("Enter numbers of inputs:"))
except Exception as Error:
    raise TypeError ("Only numbers Permited")

payload = {'id': ID_user, 'holdthedoor': 'Submit'}
URL = "http://158.69.76.135/level0.php"
errors = 0
request = 0
current_request = 0

for index in range(current_request, num_requests):
    r = requests.post(URL, data=payload)
    if r.status_code == 200:
        print("Request accepted {}".format(index))
        request += 1
    if r.status_code != 200:
        print("failed request number {}".format(index))
        errors += 1

print()
print("Resume:")
print("Total requests {}".format(request))
print("failed requests {}".format(errors))
