#metadateador Losada
import pandas as pd
import openpyxl as op
import os

for root, dirs, files in os.walk(".", topdown=False):
	print(files)	
