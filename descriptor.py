#descriptor

import resquests
import re
import pandas as pd
import json
import openpyxl as op

eml = pd.read_csv(r"C:/Users/David/Desktop/EML.txt", sep=';',error_bad_lines=False)

def descargar_datos(mla):
	token="APP_USR-4726037063911819-072418-feae59075843a687efbfd352d7cab455-553279780"
	url="https://api.mercadolibre.com/items/"+mla
	headers = {"Authorization": str("Bearer "+token),"Content-type": "application/json" }

	req = requests.get(url, headers=headers)
	print(req)
	if req.status_code == 200:
		regjson=req.json()
		atributos=regjson['attributes']
		sku=atributos[-1]['value_name']
		imag=[]
		return(sku)
def recolectar_datos(sku,mla):
	fila= eml[eml.ISBN==sku]
	pretitulo=fila.iat[0,1]
	preautor=fila.iat[0,2]
	editorial=(fila.iat[0,3]).strip()
	preprecio=str(fila.iat[0,28])
	reprecio=preprecio.split('.')
	precio=reprecio[0]
	tema=(fila.iat[0,5]).strip()
	stock=fila.iat[0,17]
	proveedor=fila.iat[0,4]
	return (pretitulo, preautor,precio,tema, stock, proveedor, editorial)		
def corrector_titulo(pretitulo):
	retitulo=re.search(r"(.*), ([LE][A-Z]\w?)(.*)", pretitulo)
	if retitulo == None:
		prepre=pretitulo
	else:
		titulo=(retitulo[2]+" "+retitulo[1]+" "+retitulo[3]).strip()
		prepre=titulo
	retitulo2=re.search(r"(.*)(/L)(.*)",prepre)
	if retitulo2 == None:
		return prepre.strip()
	else:
		titulo=(retitulo2[1]+retitulo2[3]).strip()
		return titulo
def corrector_autor(preautor):	
	reautor = re.search(r"(.*), (.*)",preautor)
	if reautor == None:
		return (preautor.strip(),preautor.strip())
	else:	
		autor=reautor[2]+" "+reautor[1]
		apellido=reautor[1]
		return (autor, apellido)
def desambiguador(proveedor, editorial,isbn):
	if "LOSADA" in proveedor:
		if "LOSADA" in editorial:
			paginas=
			formato=
			sinopsis=

class Escrapeadoreditorial:
	def __init__(self,url,busqueda,item,paginas,tapa,tamaño,sinopsis)
		
	def scrappenguin():


def eje(mla):
	sku=descargar_datos(mla)



excel_lista=op.load_workbook("TITUcambio.xlsx")
hoja_lista=excel_lista["Hoja1"]
cantidad=len(hoja_lista["A"])
print(cantidad)
for x in range(1,cantidad+1):
	item=hoja_lista.cell(row=x,column=1).value