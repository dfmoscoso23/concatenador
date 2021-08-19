#claseescrapeadora
import requests
from bs4 import BeautifulSoup
import re

peng=("https://www.penguinlibros.com/ar/",
	"module/elastico/elasticosearch?fc=module&module=elastico&controller=elasticosearch&s=",
	"find('div', class_='thumbnail-container').a['href']",
	"comic/135750-tomar-refugio-9788416131495")

class Escrap:
	def __init__(self,url,busquedaurl,busqueda,sku):#,item,paginas,tapa,tamaño,sinopsis):
		self.url=url
		self.busquedaurl=busquedaurl
		self.busqueda=busqueda
		self.sku=sku
		self.alianza=Escrap.extractorAlianza(Escrap.buscadorAlianza(sku))
		#self.item=item
		#self.paginas=paginas
		#self.tapa=tapa
		#self.tamaño=tamaño
		#self.sinopsis=sinopsis
	def desambiguador(editorial,sku):
		try:
			if "ALIANZA" in editorial:
				return Escrap.extractorAlianza(Escrap.buscadorAlianza(sku))
			elif "LOSADA" in editorial:
				return Escrap.extractorLosada(Escrap.buscadorLosada(sku))
			elif "TECNOS" in editorial:
				return Escrap.extractorTecnos(Escrap.buscadorTecnos(sku))
			elif "CATEDRA" in editorial:	
				return Escrap.extractorCatedra(Escrap.buscadorCatedra(sku))
			elif "AIQUE" in editorial:
				return Escrap.extractorAique(Escrap.buscadorAique(sku))
			elif "LAROUSSE" in editorial:	
				pass
		except AttributeError:
			print("No está en la página")		
	def busquedalibro(url,busqueda,busquedaurl,sku):
		urlcomb=str(url)+str(busquedaurl)+str(sku)
		req=requests.get(urlcomb)
		soup = BeautifulSoup(req.text, 'lxml')
		urlitem= getattr(soup,busqueda)
		print(urlitem)
		pato ="pato"
		prueba=getattr(pato,'title')
		print(prueba)
		if url in str(urlitem):
			it = str(urlitem).split(url)
			item=it[1]
		else:
			item = urlitem		
		return item

	def extractor(url, item):
		urlcomb=str(url)+str(item)
		req=requests.get(urlcomb)
		soup = BeautifulSoup(req.text, 'lxml')
		indice=soup.find(dl, class_="caracteristicas-prod data-sheet")

	def buscadorAlianza(sku):
		url='https://www.alianzaeditorial.es/busqueda.php?tipobusqueda=busqueda&precioMin=0&precioMax=200&texto='+str(sku)
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		busca=soup.find('div', class_="book-list-item-image")
		href=busca.a['href']
		urlo='https://www.alianzaeditorial.es'+href
		return urlo
	def extractorAlianza(urlo):
		ro = requests.get(urlo)
		soup = BeautifulSoup(ro.text, 'lxml')
		primer_grupo=soup.find('div', class_="main-hero detail")
		info_basica=primer_grupo.find('div', class_="book-info")
		titulo=info_basica.h1.text
		autor=info_basica.a.text
		info_detallada=soup.find('div', class_="block-info")
		data=info_detallada.find('div', class_="data")
		datali=data.find_all('li', class_="data-item")
		formato=datali[5].find('p', class_="value").text
		paginas=datali[6].find('p', class_="value").text
		bloquedescripcion=soup.find('p', class_="description-text").text
		return paginas, formato, bloquedescripcion	
	def buscadorCatedra(sku):
		url='https://www.catedra.com/busqueda.php?tipobusqueda=busqueda&precioMin=0&precioMax=200&texto='+str(sku)
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		busca=soup.find('div', class_="book-list-item-image")
		href=busca.a['href']
		urlo='https://www.catedra.com'+href
		return urlo
	def extractorCatedra(urlo):
		ro = requests.get(urlo)
		soup = BeautifulSoup(ro.text, 'lxml')
		primer_grupo=soup.find('div', class_="main-hero detail")
		info_basica=primer_grupo.find('div', class_="book-info")
		titulo=info_basica.h1.text
		autor=info_basica.a.text
		info_detallada=soup.find('div', class_="block-info")
		data=info_detallada.find('div', class_="data")
		datali=data.find_all('li', class_="data-item")
		formato=datali[5].find('p', class_="value").text
		paginas=datali[6].find('p', class_="value").text
		bloquedescripcion=soup.find('p', class_="description-text").text
		return paginas, formato, bloquedescripcion
	def buscadorLosada(sku):
		raw_isbn=str(sku)
		isbn_guinado=raw_isbn[0:3]+"-"+raw_isbn[3:6]+"-"+raw_isbn[6:8]+"-"+raw_isbn[8:12]+"-"+raw_isbn[-1]
		url='http://www.editoriallosada.com/search/content/'+isbn_guinado
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		busca=soup.find('div', class_="ds-2col-fluid node node-libro node-teaser view-mode-teaser clearfix")
		href=busca.h2.a['href']
		urlo='http://www.editoriallosada.com'+href
		return urlo
	def extractorLosada(urlo):
		ro = requests.get(urlo)
		soupo = BeautifulSoup(ro.text, 'lxml')
		div_paginas=soupo.find('div', class_="field field-name-field-paginas field-type-text field-label-inline clearfix")
		paginas=div_paginas.find('div', class_="field-item even")
		sinopsis=soupo.find('div', class_="lead")
		div_formato=soupo.find('div', class_="field field-name-field-formato field-type-text field-label-hidden")
		formato=div_formato.find('div', class_="field-item even").text
		return paginas, formato, sinopsis
	def buscadorAique(sku):
		raw_isbn=str(sku)
		isbn_guinado=raw_isbn[0:3]+"-"+raw_isbn[3:6]+"-"+raw_isbn[6:8]+"-"+raw_isbn[8:12]+"-"+raw_isbn[-1]
		url='http://www.aique.com.ar/search/content/'+isbn_guinado
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		busca=soup.find('div', class_="ds-2col-fluid node node-libro node-teaser view-mode-teaser clearfix")
		href=busca.h2.a['href']
		urlo='http://www.aique.com.ar'+href
		return urlo
	def extractorAique(urlo):
		ro = requests.get(urlo)
		soupo = BeautifulSoup(ro.text, 'lxml')
		div_paginas=soupo.find('div', class_="field field-name-field-paginas field-type-text field-label-inline clearfix")
		paginas=div_paginas.find('div', class_="field-item even")
		sinopsis=soupo.find('div', class_="lead")
		div_formato=soupo.find('div', class_="field field-name-field-formato field-type-text field-label-hidden")
		formato=div_formato.find('div', class_="field-item even").text
		return paginas, formato, sinopsis
	def buscadorTecnos(sku):
		url='https://www.tecnos.es/listado.php?titulo=&autor=&isbn='+str(sku)+'&codigo_comercial=&coleccion=&formato=&origen=busqueda_avanzada'
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		busca=soup.find('div', class_="listado")
		href=busca.a['href']
		urlo='https://www.tecnos.es'+href[2:]
		return urlo			
	def extractorTecnos(urlo):
		r = requests.get(urlo)
		soup = BeautifulSoup(r.text, 'lxml')
		sinopsis=soup.find('div', class_='resena').p.text
		datos_box=soup.find('div', class_='datos').contents
		paginas=datos_box[6]
		preformato=re.search(r'(\w*)$',datos_box[26])
		formato=preformato[1]
		return paginas, formato, sinopsis



print(Escrap.desambiguador('TECNOS',9788430944200))

#Escrap.busquedalibro(peng1,peng2,peng3,peng4)		
		
