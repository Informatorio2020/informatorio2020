#Ejercicio 3:
# Haz una clase llamada Persona que siga las siguientes condiciones:
# Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No
# queremos que se accedan directamente a ellos.
# Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0
# números, cadena vacía para String, etc.).
# Se debe implantar el constructor de la clase.
#
# Los métodos que se implementarán son:
#       ● calcularIMC(): calculará si la persona está en su peso ideal (peso en kg/(altura^2 en
#           m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si
#           devuelve un número entre 20 y 25 (incluidos), significa que está por debajo de su
#           peso ideal la función devuelve un 0 y si devuelve un valor mayor que 25 significa
#           que tiene sobrepeso, la función devuelve un 1.
#       ● esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
#       ● recuperar_infomacion(): devuelve toda la información del objeto.
#       ● generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su
#           número su letra correspondiente. Este método será invocado cuando se construya el
#           objeto. No será visible al exterior.
#       ● Métodos modificadores de cada parámetro, excepto de DNI.
# Ahora, crea una clase ejecutable que haga lo siguiente:
#       1. Pide por teclado el nombre, la edad, sexo, peso y altura.
#       2. Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables
#           pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso
#           y la altura y el último por defecto, para este último utiliza los métodos set para darle
#           a los atributos un valor.
#       3. Para cada objeto, deberá comprobar si está en su peso ideal, tiene sobrepeso o por
#           debajo de su peso ideal con un mensaje.
#       4. Indicar para cada objeto si es mayor de edad.
#       5. Por último, mostrar la información de cada objeto.

from enum import Enum
from random import randint


class Sexo(Enum):
    H = 1
    M = 2


class Persona:

    def __init__(self, nombre: str = "", edad: int = 0,
                 sexo: Sexo = None, peso: float = 0, altura: float = 0):
        self.__DNI = self.__generaDNI()
        self.__Nombre = nombre
        self.__Edad = edad
        self.__Sexo = sexo,
        self.__Peso = peso
        self.__Altura = altura

    def calcularIMC(self):
        resultado = self.__Peso / (self.__Altura ** 2)

        return -1 if resultado < 20 else 0 if 20 <= resultado <= 25 else 1

    def esMayorDeEdad(self):
        return self.__Edad >= 18

    def recuperar_infomacion(self):
        return self.__str__()

    def __generaDNI(self):
        return randint(10000000, 50000000)

    def modificarNombre(self, valor: str):
        self.__Nombre = valor

    def modificarEdad(self, valor: int):
        self.__Edad = valor

    def modificarSexo(self, valor: Sexo):
        self.__Sexo = valor

    def modificarPeso(self, valor: float):
        self.__Peso = valor

    def modificarAltura(self, valor: float):
        self.__Altura = valor

    def __str__(self):
        return f"{self.__Nombre}[{self.__DNI}]. " \
               f"{self.__Edad} años, {self.__Sexo}. " \
               f"Peso: {self.__Peso}. Altura: {self.__Altura} "


mensaje = lambda valor: \
    "Muy por debajo del peso normal" if valor == -1 else \
    "Peso por debajo del ideal" if valor == 0 else \
    "Sobrepreso"

comprobarEdad = lambda valor: "Es mayor de edad" if valor is True else "Es menor de edad"

# Ahora, crea una clase ejecutable que haga lo siguiente:
#       1. Pide por teclado el nombre, la edad, sexo, peso y altura.
nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese la edad: "))
sexo = Sexo.H if input("1. Hombre || 2. Mujer: ") == "1" else Sexo.M
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en m: "))


#       2. Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables
#           pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso
#           y la altura y el último por defecto, para este último utiliza los métodos set para darle
#           a los atributos un valor.
Alfa = Persona(nombre, edad, sexo, peso, altura)
Beta = Persona(nombre, edad, sexo)
Beta.modificarPeso(randint(50, 150))
Beta.modificarAltura(randint(1, 2))
Gamma = Persona()
Gamma.modificarNombre(nombre)
Gamma.modificarEdad(randint(1, 50))
Gamma.modificarSexo(sexo)
Gamma.modificarPeso(randint(50, 150))
Gamma.modificarAltura(randint(1, 2))


#       3. Para cada objeto, deberá comprobar si está en su peso ideal, tiene sobrepeso o por
#           debajo de su peso ideal con un mensaje.
print(mensaje(Alfa.calcularIMC()))
print(mensaje(Beta.calcularIMC()))
print(mensaje(Gamma.calcularIMC()))


#       4. Indicar para cada objeto si es mayor de edad.
print(comprobarEdad(Alfa.esMayorDeEdad()))
print(comprobarEdad(Beta.esMayorDeEdad()))
print(comprobarEdad(Gamma.esMayorDeEdad()))


#       5. Por último, mostrar la información de cada objeto.
print(Alfa)
print(Beta)
print(Gamma)



