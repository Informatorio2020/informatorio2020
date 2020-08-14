#DESAFÍO 5
# Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la 
# vía pública.
# Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico
# de 5 dígitos a la Central con el siguiente significado:
#   3 letras: Correspondientes a la patente.
#   Del valor numérico:
#       Los 3 primeros números corresponden a la patente
#       El 4 número indica
#           1- Tiró basura a la vía pública
#           0 - No tiró basura a la vía pública
#       El 5 número indica
#           1- Ya había sido multado el vehículo
#           0 - Vehículo sin multas.
# Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.

from os import system

class Patente:
    patenteOriginal = None
    datos = None
    tiroBasura = False
    multado = False

    def __init__(self, datos, tiroBasura, multado):
        self.patenteOriginal = datos
        self.tiroBasura = tiroBasura
        self.multado = multado
        #Existe un error de formato porque 0 no puede ser negativo, entonces al castear el numero se elimina el - al 0
        self.datos = self.patenteOriginal + (str(-1) if (self.tiroBasura) else str(-0))
        self.datos = self.datos + (str(-1) if (self.multado) else str(-0))
        print("")

    def informe(self):
        print(f"Patente del vehiculo: {self.datos}")
        print(f"Patente del vehiculo: {self.patenteOriginal}")
        print(f"Este vehiculo {'ha tirado basura' if (self.tiroBasura) else 'no ha tirado basura'}")
        print(f"Este vehiculo {'posee multas' if (self.multado) else 'no posee multas'}\n\n")

vehiculos = []
contadorBasura = 0
contadorMultas = 0

while(True):
    datos = input("Ingrese la patente del vehiculo: ")

    basura = input("¿El conductor ha tirado basura? S/N (Por defecto No): ")

    multa = input("¿El conductor posee una multa? S/N (Por defecto No): ")

    if(basura.lower() == "s" or basura.lower() == "si"):
        basura = True
    else:
        basura = False

    if(multa.lower() == "s" or multa.lower() == "si"):
        multa = True
    else:
        multa = False

    vehiculos.append(Patente(datos, basura, multa))

    opcion = input("¿Desea registrar otro automotor? S/N (Por defecto Si): ")

    if(opcion.lower() == "n" or opcion.lower() == "no"):
        break
    else:
        system("cls")

system("cls")

for actual in vehiculos:
    if(actual.tiroBasura):
        contadorBasura += 1
        if(actual.multado):
            contadorMultas += 1
    actual.informe()

print(f"\n\nSe contabilizaron {len(vehiculos)}\nDe estos, {contadorBasura} conductores tienen antecedentes de tirar basura\nDe los que tiraron basura, el {round((contadorMultas / contadorBasura) * 100, 2)}% poseen multas")

input("\nFin")
    