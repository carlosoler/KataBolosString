class Bolera:

    def calcularPuntuacion(self, partida):
        suma = 0
        for index, tirada in enumerate(partida):
            if tirada == '/':#semi-pleno
                suma = suma - int(partida[index-1]) + 10 + int(partida[index+1])
            elif tirada == 'X':#pleno
                suma = suma + 10 + int(partida[index+1]) + int(partida[index+2])
            elif tirada != '-':
                suma = suma + int(tirada)
        return suma