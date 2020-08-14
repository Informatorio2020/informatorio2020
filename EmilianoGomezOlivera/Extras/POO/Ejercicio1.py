class Cuenta:

    def __init__(self, titular: str, cantidad: float = 0):
        self.__Titular = titular
        self.__Cantidad = cantidad

    def obtenerInformacion(self):
        return self.__str__()

    def modificarInformacion(self, nuevoTitular: str = None, nuevaCantidad: float = None):
        if nuevoTitular is not None:
            self.__Titular = nuevoTitular

        if nuevaCantidad is not None:
            self.__Cantidad = nuevaCantidad

    def ingresar(self, monto: float):
        if monto > 0:
            self.__Cantidad += monto

    def retirar(self, monto: float):
        if monto < 0:
            self.__Cantidad -= (monto * -1)
        else:
            self.__Cantidad -= monto

        if self.__Cantidad < 0:
            self.__Cantidad = 0

    def Titular(self):
        return self.__Titular

    def Cantidad(self):
        return self.__Cantidad

    def __str__(self):
        return f"Titular de la cuenta: {self.__Titular}. Dinero en la cuenta: ${self.__Cantidad}"