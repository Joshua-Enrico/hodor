#!/usr/bin/python3
"""
Requests a N numbers of times
"""
import requests
from bs4 import BeautifulSoup

ID_user = "3014"
num_request = 98
errors = 0
request = 0
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
current_request = 0
URL = "http://158.69.76.135/level4.php"
proxy_sites = ["https://www.free-proxy-list.net/", "https://www.us-proxy.org/"]
rotate = 0
z = 0

header = {
    "user-Agent": user_agent,
    "referer": URL
}
payload = {
            'id': ID_user,
            'holdthedoor': 'Submit',
            'key': ''
            }

proxy = {
    "http": ''
}

for index in range(num_request):
    session = requests.session()
    page = session.get(proxy_sites[rotate])
    rotate = 1 if rotate == 0 else 0
    soup = BeautifulSoup(page.text, "html.parser")
    proxy_list = soup.find("tbody").find_all("tr")

    for ip in proxy_list:
        proxy["http"] = "http://" + ip.find("td").text
        print("Cheking {}".format(proxy["http"]))
        z += 1
        try:
            session = requests.session()
            page = session.get(URL, headers=header, proxies=proxy, timeout=5)

            soup = BeautifulSoup(page.text, "html.parser")
            hidden_value = soup.find("form")

            hidden_value = hidden_value.find("input", {"type": "hidden"})

            hidden_value = hidden_value["value"]
            payload["key"] = hidden_value

            r = session.post(URL, headers=header, data=payload, proxies=proxy, timeout=5)
            if r.status_code == 200:
                print("Request accepted {}".format(request), end='\r')
                request += 1
            print("3")
            if r.status_code != 200:
                print("failed request number {}".format(errors), end='\r')
                errors += 1
        except:
            print("failed")
    if request == 98:
        break

print()
print()
print("Resume:")
print("Total requests {}".format(index + 1))
print("succesful requests {}".format(request))
print("failed requests {}".format(errors))
print("total ip used {}".format(z))
