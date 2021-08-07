#Flex-controlversion2.1
from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import openpyxl as op
from datetime import date, timedelta, datetime
#from fpdf import FPDF
import requests
token="APP_USR-4726037063911819-070713-e7db9d3b363aad233b270a65b1749e0b-553279780"
#url="https://api.mercadolibre.com/orders/search?seller=553279780&order.date_created.from=2021-06-25T13:00:00.000-00:00&order.date_created.to=2021-06-30T13:00:00.000-00:00"
url="https://api.mercadolibre.com/orders/"+str(4694579845)
headers={'Authorization': 'Bearer '+token}

r = requests.get(url, headers=headers)

print(r)

if r.status_code == 200:
	rjson=r.json()
	#results=rjson['results']
	#paging=rjson['paging']
	#display=rjson['display']
	for key, value in rjson.items():
		print(key)
		print("x>")
		print(value)
	dia_cierre=rjson['date_closed']
	dia_creacion=rjson['date_created']
	print(dia_cierre)
	print(dia_creacion)
	#print(paging)
	#print(results[0])
	#item=results[-5]
	#for key in item:
		#print(key)
	#ident=item['id']
	#print(ident)

	shipping=rjson['shipping']
	url="https://api.mercadolibre.com/shipments/"+str(shipping['id'])
	#url="https://api.mercadolibre.com/shipments/"+str(40678827291)
	headers={'Authorization': 'Bearer '+token}
	r2 = requests.get(url, headers=headers)
	if r2.status_code == 200:
		rjson2=r2.json()
		logistic=rjson2['logistic_type']
		if logistic == 'self_service':
			option=rjson2['shipping_option']
			costo=option['list_cost']
			#print(str(shipping['id'])+">"+str(costo))
		for key, value in rjson2.items():
			print(key)
			print(">>>")
			print(value)
