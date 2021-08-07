#losapeando
import requests
from bs4 import BeautifulSoup

print("inserte ISBN:")
raw_isbn=input()

isbn_guinado=raw_isbn[0:3]+"-"+raw_isbn[3:6]+"-"+raw_isbn[6:8]+"-"+raw_isbn[8:12]+"-"+raw_isbn[-1]
print(isbn_guinado)

url='http://www.editoriallosada.com/search/content/'+isbn_guinado
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
busca=soup.find('div', class_="ds-2col-fluid node node-libro node-teaser view-mode-teaser clearfix")
href=busca.h2.a['href']
urlo='http://www.editoriallosada.com'+href
print(urlo)
ro = requests.get(urlo)
soupo = BeautifulSoup(ro.text, 'lxml')
div_formato=soupo.find('div', class_="field field-name-field-formato field-type-text field-label-hidden")
formato=div_formato.find('div', class_="field-item even")
print(formato.text)
div_paginas=soupo.find('div', class_="field field-name-field-paginas field-type-text field-label-inline clearfix")
paginas=div_paginas.find('div', class_="field-item even")
print(paginas.text)
sinopsis=soupo.find('div', class_="lead")
print(sinopsis.text)
"""
print(soupo.title)
print(soupo.h1)
print(soupo.h2)
print(soupo.h3)
sinopsis=soupo.find_all('div', class_="lead")
isbn=soupo.find_all('div', class_="field field-name-field-isbn field-type-text field-label-inline clearfix")
sinopsis_larga=soupo.find('div', class_="group-right")
print(sinopsis)
print(isbn)
print(sinopsis_larga)

buca=soup.find('div', class_="ds-2col-fluid node node-libro node-teaser view-mode-teaser clearfix")
print(buca.h2.a)
href=buca.h2.a['href']
print(href)
"""