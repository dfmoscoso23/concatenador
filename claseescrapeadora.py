#claseescrapeadora
import requests
from bs4 import BeautifulSoup
"""
de=
peng=("https://www.penguinlibros.com/ar/",
	"module/elastico/elasticosearch?fc=module&module=elastico&controller=elasticosearch&s=",
	find('div', class_="thumbnail-container").a['href'],
	"comic/135750-tomar-refugio-9788416131495")
"""
class Escrap:
	def __init__(self,url,busquedaurl,busqueda):#,item,paginas,tapa,tamaño,sinopsis):
		self.url=url
		self.busquedaurl=busquedaurl
		self.busqueda=busqueda
		#self.item=item
		#self.paginas=paginas
		#self.tapa=tapa
		#self.tamaño=tamaño
		#self.sinopsis=sinopsis

	def busquedalibro(url,busqueda,busquedaurl,sku):
		urlcomb=str(url)+str(busquedaurl)+str(sku)
		req=requests.get(urlcomb)
		soup = BeautifulSoup(req.text, 'lxml')
		urlitem=soup.busqueda
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
		
		
