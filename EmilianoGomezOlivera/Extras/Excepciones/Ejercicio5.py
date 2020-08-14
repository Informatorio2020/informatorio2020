#Ejercicio 5:
# Realizar un programa que solicite un valor entero y lo devuelve.Si el valor ingresado no es
# entero, de 5 intentos para ingresarlo correctamente, y de no ser así, lanza una excepción.

class NotIntegerException(Exception):
    def __init__(self):
        super().__init__("The user failed to enter an integer after 5 attempts.")

def numero():
    i = 0
    x = None

    while(i < 5):
        x = input("Ingrese un numero entero: ")

        if(x.isdigit()):
            break
        else:
            x = None
            i += 1
    
    if(x == None):
        raise NotIntegerException

numero()

input("\nFin")