#Pandeando
import pandas as pd 
import numpy as np
hoja_csv= pd.read_csv(r'EML.txt', sep=';')

#print(hoja_csv.info())

print(hoja_csv.loc[5,'ISBN'])

isbn2=hoja_csv.loc[10,'ISBN']
print(type(isbn2))
print(isbn2)
tit="MARIANELA"
noes=[]
isbn="9788420633763"
for x in range(306):
	if hoja_csv.loc[x,'ISBN']== isbn2:
		print(x)
	else:
		noes.append(x)
print(len(noes))
pd.to_numeric(hoja_csv['ISBN'])
isbn2=hoja_csv.loc[10,'ISBN']
print(type(isbn2))
for x in range(306):
	val = hoja_csv.loc[x,'ISBN']
	#val= cont.item()
	if val == int(isbn):
		print(x)
	else:
		noes.append(x)
print(len(noes))
for x in range(306):
	if hoja_csv.loc[x,'Titulo']== "MARIANELA":
		print(x)
	else:
		noes.append(x)
print(len(noes))		
#ind=hoja_csv["Titulo"].str.find(tit)
print("-----")
print(hoja_csv.query('ISBN == 9788420634197', inplace = True))
fila= hoja_csv[hoja_csv.ISBN==isbn]
print(fila)
