class Bolera:

    def calcularPuntuacion(self, partida):
        suma = 0
        for tirada in partida:
            if tirada != '-':
                suma = suma + int(tirada)
        return suma