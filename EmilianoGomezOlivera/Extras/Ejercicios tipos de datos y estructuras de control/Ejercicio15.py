#Ejercicio 15:
# Escribí un programa para solicitar al usuario que ingrese 
# números enteros positivos (la cantidad que ingresará no se 
# conoce y la decide el usuario). La lectura de números 
# finalizará cuando el usuario ingrese el número -1. Por cada 
# número ingresado, mostrar la cantidad de dígitos pares y la 
# cantidad de dígitos impares que tiene. Al finalizar, mostrar 
# cuántos números múltiplos de 3 ingresó el usuario. 

from os import system

# Cree una clase para agilizar las operaciones
class Cifra:
    #Los campos de la clase
    numero = 0
    pares = 0
    impares = 0
    multiplo = False

    # Constructor de la calse
    def __init__(self, numero):
        self.numero = numero
        self.pares = self.contarPares()
        self.impares = self.contarImpares()
        self.multiplo = "Es multiplo de 3" if (numero % 3 == 0) else "No es multiplo de 3"

    # Funciones de la clase
    def contarPares(self):
        cantidad = 0
        aux = self.numero

        while(True):
            digito = aux % 10
            cantidad += 1 if (digito % 2 == 0) else 0
            aux = int(aux / 10)

            if(aux == 0):
                break
        
        return cantidad

    def contarImpares(self):
        cantidad = 0
        aux = self.numero

        while(True):
            digito = aux % 10
            cantidad += 1 if (digito % 2 != 0) else 0
            aux = int(aux / 10)

            if(aux == 0):
                break
        
        return cantidad

    # Metodo de funcionamiento igual al toString() de Java o C#
    def __str__(self): # CORREGIR
        mensaje = f"Numero: {self.numero} se compone de {self.pares} pares y {self.impares} impares. {self.multiplo}\n\n"
        return mensaje

entrada = None
numeros = []

# Bucle de operaciones
while(True):
    entrada = input("Ingrese un numero (-1 para finalizar): ")

    if(entrada == "-1"):
        break
    else:
        try:
            entrada = int(entrada)
            # Agrego a la lista una nueva instancia del objeto cifra
            numeros.append(Cifra(entrada))
            system("cls")
        except ValueError:
            print(f"Error en el casteo de '{entrada}': No se puede convertir al tipo numerico")
            entrada = None

system("cls")
print("Se ingresaron los siguientes numeros: \n")

# Finalmente se recorre la lista y se llama al metodo __str__() del objeto 
for i in range(len(numeros)):
    print(numeros[i])

input("Fin")