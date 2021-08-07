#apeando

import requests
import json
url="https://api.mercadolibre.com/users/test_user"
url="https://api.mercadolibre.com/items/MLA885273386"

token="APP_USR-4726037063911819-071613-0cf2428ac2ebd1b7598da2eb0242c60a-553279780"

headers = {"Authorization": str("Bearer "+token),"Content-type": "application/json" }

#data= {"site_id":"MLA"}

req = requests.get(url, headers=headers)

print(req)
#print(req.content)
if req.status_code == 200:
	regjson=req.json()
	for key in regjson:
		print(key)
	print("-------")

	#categoria=regjson['category_id']
	#print(categoria)
	#print("-------")	
	#listing=regjson['listing_type_id']
	#print(listing)	
	#print("-------")
	#imagenes=regjson['pictures']
	#print(type(imagenes))
	#for key in imagenes:
		#print(key)	
		#print("-------")
	#print(imagenes[0]['url'])
		
	atributos=regjson['attributes']
	print(type(atributos))
	for key in atributos:
		print(key)	
		print("-------")
	print(atributos[-1]['value_name'])
	#envio=regjson['shipping']
	#print(type(envio))
	#for key, value in envio.items():
		#print(key+"<<<")
		#print(value)	
		#print("-------")
	#print(envio)
"""
hola="hola"

if isinstance(hola,"str"):
	print("si")
else:
	print("no")	
print(type(type(hola)))		
"""