class Vehiculo:

    def __init__(self, color: str, cantidadRuedas: int):
        """
        :param color: Color del vehiculo
        :param cantidadRuedas: Cantidad de ruedas del vehiculo
        """
        self.__Color = color
        self.__Ruedas = cantidadRuedas

    def cambiarColor(self, nuevoColor):
        """
        Funcion que permite cambiar el atributo Color del objeto

        :param nuevoColor: Color al que se actualizara el vehiculo
        :return: None
        """
        self.__Color = nuevoColor

    def cambiarRuedas(self, cantidad):
        """
        Funcion que permite cambiar el atributo Ruedas del objeto

        :param cantidad: Cantidad de ruedas que tendra el vehiculo
        :return: None
        """
        self.__Ruedas = cantidad

    def color(self):
        """
        Devuelve el color

        :return: self.Color
        """

        return self.__Color

    def ruedas(self):
        """
        Devuelve la cantidad de ruedas

        :return: self.Ruedas
        """

        return self.__Ruedas

class Coche (Vehiculo):

    def __init__(self, color: str, cilindrada: int):
        super().__init__(color, 4)
        self.__Velocidad = 0
        self.__Cilindrada = cilindrada

    def cilindrada(self):
        """
        Devuelve la cilindrada del coche

        :return: self.Cilindrada
        """

        return self.__Cilindrada

    def cambiarCilindrada(self, nuevoValor: int):
        """
        Cambia el valor del atributo Cilindrada del objeto

        :param nuevoValor: Nuevo valor para la cilindrada
        :return: None
        """
        self.__Cilindrada = nuevoValor

    def cambiarVelocidad(self, kmh: float):
        """
        Cambia el valor del atributo Velocidad del objeto

        :param kmh: Nuevo valor para la velocidad
        :return: None
        """

        self.__Velocidad = kmh

    def velocidad(self):
        """
        Devuelve la velocidad del coche

        :return: self.Velocidad
        """

        return self.__Velocidad