import unittest
from Bolera import *

class MyTestCase(unittest.TestCase):
    def test_iniciarPartida(self):
        bolera = Bolera()

    def test_calculaPuntuacion_0(self):
        bolera = Bolera()
        partida = '--------------------'
        resultado = bolera.calularPuntuacion(partida)
        self.assertEqual(0, resultado)


if __name__ == '__main__':
    unittest.main()
