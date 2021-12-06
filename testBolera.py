import unittest
from Bolera import *

class MyTestCase(unittest.TestCase):
    def test_iniciarPartida(self):
        bolera = Bolera()

    def test_calculaPuntuacion_0(self):
        bolera = Bolera()
        partida = '--------------------'
        resultado = bolera.calcularPuntuacion(partida)
        self.assertEqual(0, resultado)

    def test_calculaPuntuacion_1(self):
        bolera = Bolera()
        partida = '11111111111111111111'
        resultado = bolera.calcularPuntuacion(partida)
        self.assertEqual(20, resultado)

    def test_calculaPuntuacion(self):
        bolera = Bolera()
        partida = '-1-1-1-1-1-1-1-1-1-1'
        resultado = bolera.calcularPuntuacion(partida)
        self.assertEqual(10, resultado)

    def test_semiPleno(self):
        bolera = Bolera()
        partida = '1/11----------------'
        resultado = bolera.calcularPuntuacion(partida)
        self.assertEqual(13, resultado)


if __name__ == '__main__':
    unittest.main()
