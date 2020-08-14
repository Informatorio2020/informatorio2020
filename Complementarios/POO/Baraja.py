PALOS = ("Espada", "Basto", "Oro", "Copa")

class Carta:

    def __init__(self, valor: str, palo: str):
        self.__Valor = valor
        self.__Palo = palo

    def __str__(self):
        return f"{self.__Valor} de {self.__Palo}"

class Baraja:

    def __init__(self):
        self.__CartasPresentes = []
        self.__CartasRepartidas = []

        for i in range(4):
            for valor in range(1, 13):
                if valor == 8 or valor == 9:
                    pass
                else:
                    self.__CartasPresentes.append(Carta(str(valor), PALOS[i]))

    def mostrarBaraja(self):
        for actual in self.__CartasPresentes:
            print(actual)

    def barajar(self):
        from random import shuffle as mezclarCartas

        mezclarCartas(self.__CartasPresentes)

    def siguienteCarta(self):
        if len(self.__CartasPresentes) > 0:
            elemento = self.__CartasPresentes.pop(0)
            self.__CartasRepartidas.append(elemento)

            return elemento
        else:
            print("No hay mas cartas")
            return None

    def cartasDisponibles(self):
        if len(self.__CartasPresentes) != 0:
            print(f"Hay {len(self.__CartasPresentes)} cartas")
        else:
            print("No hay mas cartas")

    def darCartas(self, cantidad: int = 1):
        reparto = []

        if cantidad > len(self.__CartasPresentes):
            print("No hay suficientes cartas")
            return None
        elif cantidad == 1:
            return self.siguienteCarta()
        else:
            for i in range(cantidad):
                actual = self.__CartasPresentes.pop(0)
                reparto.append(actual)
                self.__CartasRepartidas.append(actual)

            return tuple(reparto)

    def cartasMonto(self):
        print("Las cartas repartadisa son:")
        for actual in self.__CartasRepartidas:
            print(actual)

    def __str__(self):
        self.mostrarBaraja()
        return "\nSe ha listado la baraja"