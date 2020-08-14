#Ejercicio 3:
# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
#       Si el primer número es mayor que el segundo, debe devolver 1.
#       Si el primer número es menor que el segundo, debe devolver -1.
#       Si ambos números son iguales, debe devolver un 0.

from os import system

def relacion(a, b):
    return (0 if (a == b) else (1 if(a > b) else -1))

while(True):
    x = input("Ingrese el primer valor: ")
    system("cls")
    y = input("Ingrese el segundo valor: ")

    try:
        x = float(x)
        y = float(y)

        system("cls")
        print(f"Resultado de la comparacion: {relacion(x, y)}")
        break
    except ValueError:
        system("cls")
        print("Error en la conversion: El valor ingresado no es un numero")

input("\nFin")
