#Ejercicio 3:
# Crearemos una clase llamada Serie con las siguientes características:
# Sus atributos son titulo, numero de temporadas, entregado, genero y creador.
# Por defecto, el número de temporadas es de 3 temporadas y entregado false. El resto de
# atributos serán valores por defecto según el tipo del atributo.
# Crear un constructor un constructor que admita los valores por defecto.
# Los métodos que se implementara serán:
#       ● Métodos get de todos los atributos, excepto de entregado.
#       ● Metodos set de todos los atributos, excepto de entregado.
#       ● Sobrescribe el método __str__.


class Serie:

    def __init__(self, titulo: str = "", temporadas: int = 3,
                 entregado: bool = False, genero: str = "", creador: str = ""):
        self.__Titulo = titulo
        self.__Temporadas = temporadas
        self.__Entregado = entregado
        self.__Genero = genero
        self.__Creador = creador

    def Titulo(self, nuevo_valor: str = ""):
        if nuevo_valor == "":
            return self.__Titulo
        else:
            self.__Titulo = nuevo_valor
            
    def Temporadas(self, nuevo_valor: str = ""):
        if nuevo_valor == "":
            return self.__Temporadas
        else:
            self.__Temporadas = nuevo_valor

    def Genero(self, nuevo_valor: str = ""):
        if nuevo_valor == "":
            return self.__Genero
        else:
            self.__Genero = nuevo_valor

    def Creador(self, nuevo_valor: str = ""):
        if nuevo_valor == "":
            return self.__Creador
        else:
            self.__Creador = nuevo_valor