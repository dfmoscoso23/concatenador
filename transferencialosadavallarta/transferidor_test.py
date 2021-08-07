#transferidor_test
import unittest
import transferidor as trans

class corrector_titulo_test(unittest.TestCase):
	def test_titulo_base(self):
		titulo="MASCARDA DE CTHULU, LA"
		self.assertEqual(trans.corrector_titulo(titulo),"LA MASCARDA DE CTHULU","MAL")
	def test_titulo_sinarticulo(self):
		titulo="MARIANELA"
		self.assertEqual(trans.corrector_titulo(titulo),"MARIANELA","MAL")
	def test_titulo_losada1(self):
		titulo="ROSA TATUADA, LA/L"
		self.assertEqual(trans.corrector_titulo(titulo),"LA ROSA TATUADA","MAL")
	def test_titulo_losada2(self):
		titulo="EN BUSCA DEL TIEMPO PERDIDO/L TOMO 1"
		self.assertEqual(trans.corrector_titulo(titulo),"EN BUSCA DEL TIEMPO PERDIDO TOMO 1","MAL")	
class corrector_autor_test(unittest.TestCase):
	def test_autor_base(self):
		titulo="ROJAS, ZULMA"
		self.assertEqual(trans.corrector_autor(titulo),("ZULMA ROJAS", "ROJAS"),"MAL")
	def test_autor_sinarticulo(self):
		titulo="DANILLUK"
		self.assertEqual(trans.corrector_autor(titulo),("DANILLUK","DANILLUK"),"MAL")
	def test_autor_dosapellidos(self):
		titulo="GARCIA MARQUEZ, GABRIEL"
		self.assertEqual(trans.corrector_autor(titulo),("GABRIEL GARCIA MARQUEZ","GARCIA MARQUEZ"),"MAL")
	def test_autor_sinstrip(self):
		titulo="LOSANO       "
		self.assertEqual(trans.corrector_autor(titulo),("LOSANO","LOSANO"),"MAL")
"""		
class corrector_condicional_test(unittest.TestCase):
	def test_autor_base(self):
		editorial="LOSADA"
		self.assertEqual(trans.condicional(1,editorial),True,"MAL")
	def test_alianza(self):
		editorial="ALIANZA"
		self.assertEqual(trans.condicional(1,editorial),False,"MAL")
	def test_alianza2(self):
		editorial="ALIANZA ESPAÑA"
		self.assertEqual(trans.condicional(1,editorial),False,"MAL")
	def test_alianza3(self):
		editorial="ALIANZA         "
		self.assertEqual(trans.condicional(1,editorial),False,"MAL")
	def test_stock(self):
		editorial="LOSADA"
		self.assertEqual(trans.condicional(0,editorial),False,"MAL")
"""
class corrector_condicional_losada_test(unittest.TestCase):
	def test_autor_base(self):
		editorial="LOSADA"
		self.assertEqual(trans.condicional_losada(editorial),False,"MAL")
	def test_alianza(self):
		editorial="ALIANZA"
		self.assertEqual(trans.condicional_losada(editorial),True,"MAL")
	def test_alianza2(self):
		editorial="ALIANZA ESPAÑA"
		self.assertEqual(trans.condicional_losada(editorial),True,"MAL")
	def test_alianza3(self):
		editorial="ALIANZA         "
		self.assertEqual(trans.condicional_losada(editorial),True,"MAL")
	def test_stock(self):
		editorial="LOSADA"
		self.assertEqual(trans.condicional_losada(editorial),False,"MAL")
	"""	
	def test_autor_sinarticulo(self):
		titulo="DANILLUK"
		self.assertEqual(trans.corrector_autor(titulo),("DANILLUK","DANILLUK"),"MAL")
	def test_autor_dosapellidos(self):
		titulo="GARCIA MARQUEZ, GABRIEL"
		self.assertEqual(trans.corrector_autor(titulo),("GABRIEL GARCIA MARQUEZ","GARCIA MARQUEZ"),"MAL")
	def test_autor_sinstrip(self):
		titulo="LOSANO       "
		self.assertEqual(trans.corrector_autor(titulo),("LOSANO","LOSANO"),"MAL")								
	"""
class control_repeticion_tester(unittest.TestCase):
	def test_normal(self):
		sku="9788479278885"
		self.assertEqual(trans.control_repeticion(sku),True,"NO está encontrando")
	def test_falsum(self):
		sku="9788446011378"
		self.assertEqual(trans.control_repeticion(sku),False,"NO está encontrando")
	def test_dudoso(self):
		sku="9788471535961"
		self.assertEqual(trans.control_repeticion(sku),True,"NO está encontrando")	
		

if __name__=='__main__':
	unittest.main()		