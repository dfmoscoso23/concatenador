#obtener Token Modulo
#Obtener Token
import requests
import json
from tkinter import*
from datetime import datetime, timedelta
def revisar_token_activo(vend):
	try:
		with open("token"+vend+".txt",'r') as filen:
			last=filen.readline(-1).split(">>")
			horatoken=last[0]
		print(horatoken)
		horatoken=datetime.strptime(horatoken,'%d/%m/%Y %H:%M:%S')
		print(horatoken)
		now=datetime.now()
		print(now)
		futuro=horatoken+timedelta(seconds=21600)
		print(futuro)
		if now < futuro:
			return last[1].strip()
		else:
			return False
	except FileNotFoundError:
		return False				
def reusar_token():
	pass
def solicitar(url, data, headers,vend):
	response = requests.post(url, headers=headers, json=data)
	if response.status_code == 200:
		resp = str(response.status_code)
		respcont = str(response.content)
		resptext = str(response.text)
		respjson = response.json()
		#st_label_rtoken.config(text="Cargado")
		token_box.insert(END, respjson['access_token'])
		f = open('token'+vend+'.txt', "w")
		#f.write(resp)
		#f.write("\t")
		now=datetime.now()
		f.write(now.strftime("%d/%m/%Y %H:%M:%S"))
		f.write(">>")
		f.write(respjson['access_token'])
		f.write("\n")
		#f.write(resptext)
		f.close()
	else:
		messagebox.showerror(message="No se pudo obtener el Token, revise el código TG")
def obtener_vendedor(token):
	token_roto=token.split("-")
	return(token_roto[-1])			
def botonear():
	url = "https://api.mercadolibre.com/oauth/token"
	headers ={'accept': 'application/json','content-type': 'application/x-www-form-urlencoded'}
	data = {
	'grant_type':'authorization_code',
	'client_id':'4726037063911819',
	'client_secret':'SKjt3ZUGtiXM90wvOn2xlvraWXEvQH2N',
	'redirect_uri':'https://localhost:30000'
	}	
	global tgbox
	cod = tgbox.get()
	data['code']=cod
	global vendedor_entry
	vend=vendedor_entry.get()
	solicitar(url, data, headers, vend)
def obtenertoken(vend):
	#Toplevel
	toplevel_obtener_token = Tk()
	toplevel_obtener_token.title("Obtener Token")
	frame_OT = Frame(toplevel_obtener_token)
	frame_OT.pack()

	copiar_label=Label(frame_OT, text="Copie esto en su navegador para obtener la autorización:")
	copiar_label.grid(column=2, row=1, padx=5, pady=5)
	copiar_entry = Entry(frame_OT, width=75)
	copiar_entry.grid(column=2, row=2, padx=5, pady=5)
	copiar_entry.insert(END, "https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=4726037063911819&state=TRE7412&redirect_uri=https://localhost:30000")
	global vendedor_entry
	vendedor_entry = Entry(frame_OT, width=5)
	vendedor_entry.grid(column=3, row=2, pady=5)
	vendedor_entry.insert(END,vend)

	label1 = Label(frame_OT, text="Ingrese TG code:")
	label1.grid(column=1, row=3, padx=5, pady=5)
	global tgbox
	tgbox = Entry(frame_OT, width=75)
	tgbox.grid(column=2, row=3, padx=5, pady=5)

	boton = Button(frame_OT, text="Obtener Token", command=botonear)
	boton.grid(column=2, row=4, padx=5, pady=5)

	label1 = Label(frame_OT, text="Token:")
	label1.grid(column=1, row=4, padx=5, pady=5)
	global token_box
	token_box = Text(frame_OT, height=5, width=65)
	token_box.grid(column=2, row=5, padx=5, pady=5)
	toplevel_obtener_token.mainloop()