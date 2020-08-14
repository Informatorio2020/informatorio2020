class Vehiculo:
    vehiculos = []

    def __init__(self, color: str, ruedas: int):
        self.__Color = color
        self.__Ruedas = ruedas
        Vehiculo.vehiculos.append(self)

    @staticmethod
    def catalogar():
        return len(Vehiculo.vehiculos)


class Coche(Vehiculo):

    def __init__(self, color: str, ruedas: int, velocidad: float, cilindrada: int):
        super(Coche, self).__init__(color, ruedas)
        self.__Velocidad = velocidad
        self.__CC = cilindrada

    def velocidad(self, valor):
        if valor < 0:
            valor *= -1

        self.__Velocidad = valor

    def cilindrada(self, valor):
        if valor < 0:
            valor *= -1

        self.__CC = valor


class Camioneta(Coche):

    def __init__(self, color: str, ruedas: int, velocidad: float, cilindrada: int, carga: int):
        super(Camioneta, self).__init__(color, ruedas, velocidad, cilindrada)
        self.__Carga = carga

    def carga(self, valor):
        if valor < 0:
            valor *= -1

        self.__Carga = valor


class Bicicleta(Vehiculo):

    def __init__(self, color: str, tipo: str = "Urbana"):
        super(Bicicleta, self).__init__(color, 2)
        self.__Tipo = "Urbana" if tipo.lower() == "urbana" else "Deportiva" if tipo.lower() == "deportiva" else "Urbana"

    def tipo(self, valor):
        return self.__Tipo
        #self.__Tipo = valor


class Motocicleta(Bicicleta):

    def __init__(self, color: str, velocidad: float, cilindrada: int):
        super(Motocicleta, self).__init__(color, 2)
        self.__Velocidad = velocidad
        self.__CC = cilindrada

    def velocidad(self, valor):
        if valor < 0:
            valor *= -1

        self.__Velocidad = valor

    def cilindrada(self, valor):
        if valor < 0:
            valor *= -1

        self.__CC = valor


a = Vehiculo("Rojo", 4)
b = Bicicleta("Roja", "Deportivsa")

print(b.tipo("a"))

