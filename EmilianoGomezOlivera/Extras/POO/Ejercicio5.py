
class Electrodomestico:

    def __init__(self,
                 precio: float = 5000, color: str = "Blanco",
                 consumoEnergetico: str = "F", peso: float = 5):
        self.__Precio = precio
        self.__Color = self.__comprobarColor(color)
        self.__ConsumoEnergetico = self.__comprobarConsumoEnergetico(consumoEnergetico)
        self.__Peso = peso

    def Precio(self):
        return self.__Precio

    def Color(self):
        return self.__Color

    def ConsumoEnergetico(self):
        return self.__ConsumoEnergetico

    def Peso(self):
        return self.__Peso

    def __comprobarConsumoEnergetico(self, valor: str):
        valores = ("A", "B", "C", "D", "E", "F")

        valor = valor.upper()

        return valor if valor in valores else "F"

    def __comprobarColor(self, valor: str):
        colores = ("Blanco", "Negro", "Rojo", "Azul", "Gris")

        valor = valor.capitalize()

        return valor if valor in colores else "Blanco"

    def precioFinal(self):
        valorConsumo = \
            {"A": 5000, "B": 4000, "C": 3000,
             "D": 2000, "E": 1000, "F": 800}
        total = self.__Precio

        if 20 <= self.__Peso <= 49:
            total += 700
        elif 50 <= self.__Peso <= 79:
            total += 900
        elif 80 <= self.__Peso:
            total += 1100
        else:
            total += 500

        return total + valorConsumo[self.__ConsumoEnergetico]

class Lavadora(Electrodomestico):

    def __init__(self,
                 precio: float = 5000, color: str = "Blanco",
                 consumoEnergetico: str = "F", peso: float = 5,
                 carga: float = 5):
        super().__init__(precio, color, consumoEnergetico, peso)
        self.__Carga = carga

    def Carga(self):
        return self.__Carga

    def precioFinal(self):
        precioCarga = 700 if self.__Carga > 30 else 0

        return super(Lavadora, self).precioFinal() + precioCarga

class Television(Electrodomestico):

    def __init__(self,
                 precio: float = 5000, color: str = "Blanco",
                 consumoEnergetico: str = "F", peso: float = 5,
                 resolucion: float = 20, tdt: bool = False):
        super().__init__(precio, color, consumoEnergetico, peso)
        self.__Resolucion = resolucion
        self.__TDT = tdt

    def Resolucion(self):
        return self.__Resolucion

    def TDT(self):
        return self.__TDT

    def precioFinal(self):
        total = super(Television, self).precioFinal()

        if self.__Resolucion > 40:
            total *= 1.3

        if self.__TDT:
            total += 700

        return total