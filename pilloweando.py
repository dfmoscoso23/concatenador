# python pillow
from PIL import Image
import os

for root, dirs,files in os.walk(".", topdown=False):
	for name in files:
		if str(name[-3:])=="jpg":
			print(name)
			im1= Image.open(name)
			width, height= im1.size
			width+=50
			height+=50
			img = Image.new(mode="RGB", size=(500, 500),color = (255, 255, 255))
			cp=img.copy()
			cp.paste(im1, (25, 25))
			cp.save("C:/Listasparasubir/"+name)