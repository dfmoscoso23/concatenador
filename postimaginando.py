#postimaginando
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
"""
url="https://postimg.cc/login"
auth = HTTPBasicAuth('pedidoslosada@gmail.com','4SsJSzhfQjL2')
req = requests.get(url, auth=auth)
print(req.status_code)
"""
url="https://postimg.cc/search/9789500394116"
token="cfa968b898a22b6c7562f65322d5f956"
headers = {"token":token}
auth = HTTPBasicAuth('pedidoslosada@gmail.com','4SsJSzhfQjL2')
req = requests.get(url, headers=headers)
print(req.status_code)
if req.status_code == 200:
	soup = BeautifulSoup(req.text, 'lxml')

	busca=soup.findAll('div', class_="container")
	for item in busca:
		print(item.text)

