#funeraria

tit = "moraleja, la/Lo"

isbnd="987894"
dic_titulo={}

def funerariat(tit, isbnd):
		colon=""
		if ',' in tit:
			titu = tit.split(',')
			arti = titu [1].strip(" ")
			titul = titu[0].strip(" ")
			largo_arit=len(arti)
			if largo_arit > 3:
					if arti[2]==" ":
						artic= arti[0]+arti[1]
					elif arti[2]=="s" or arti[2]=="o" or arti[2]=="a":
						artic= arti[0]+arti[1]+arti[2]
						colon=arti[3:]
					elif arti[2]=="/":
						artic= arti[0]+arti[1]
					else:
						artic= arti[0]+arti[1]
						colon=arti[3:]			
			else:
				if arti[1]==" ":
					artic=	arti[0]
				elif arti[1]=="a" or arti[1]=="l" or arti[1]=="o":
					artic= arti[0]+arti[1]
				else:
					artic=""				
			if len(colon)>0:
				titulo = artic + " " + titul+" "+colon
			else:
				titulo = artic + " " + titul
		else:
			titulo = tit
		tituloo = titulo.title()
		titulod = tituloo.strip()
		dic_titulo[isbnd] = titulod
funerariat(tit, isbnd)
print(dic_titulo)
tit = "ciudad de las moscas, los/Losada tomo VD"

isbnd="987894543"
funerariat(tit, isbnd)
print(dic_titulo)

tit = "musicas en la sociudad,las tomo III"

isbnd="98789454345"
funerariat(tit, isbnd)
for dic,titulo in dic_titulo.items():
	print(dic, titulo)

	
