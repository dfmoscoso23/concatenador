#Flex-controlversion2.1
from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import openpyxl as op
from datetime import date, timedelta, datetime
#from fpdf import FPDF
import requests
token="APP_USR-4726037063911819-063016-a63a574dedfae71d38f4a1345f472a39-736684164"
url="https://api.mercadolibre.com/orders/search?seller=736684164&order.date_created.from=2021-06-29T13:00:00.000-00:00&order.date_created.to=2021-06-30T13:00:00.000-00:00"

headers={'Authorization': 'Bearer '+token}

r = requests.get(url, headers=headers)

print(r)
if r.status_code == 200:
	rjson=r.json()
	results=rjson['results']
	#paging=rjson['paging']
	#display=rjson['display']
	#for key in rjson:
		#print(key)
	#print(paging)
	#print(results[0])
	for item in results:
		shipping=item['shipping']
		url="https://api.mercadolibre.com/shipments/"+str(shipping['id'])
		headers={'Authorization': 'Bearer '+token}
		r2 = requests.get(url, headers=headers)
		if r2.status_code == 200:
			rjson2=r2.json()
			logistic=rjson2['logistic_type']
			if logistic == 'self_service':
				option=rjson2['shipping_option']
				costo=option['list_cost']
				print(str(shipping['id'])+">"+str(costo))
	for key, value in rjson2.items():
		print(key)
		print(">>>")
		print(value)
