#transferidor_test
import unittest
import transferidor

class corrector_titulo_test(unittest.TestCase):
	def test_titulo_base(self):
		titulo="MASCARDA DE CTHULU, LA"
		self.assertEqual(corrector_titulo_test(titulo),"LA MASCARDA DE CTHULU","MAL")