#Ejercicio 1:
# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectángulo a partir 
# de una base y una altura. 

from os import system

def area_rectangulo(base, altura):
    return round(base * altura, 2)

while(True):
    valorBase = input("Ingrese el valor de la base del rectangulo: ")
    system("cls")
    valorAltura = input("Ingrese el valor de la altura del rectangulo: ")

    try:
        valorBase = float(valorBase)
        valorAltura = float(valorAltura)

        system("cls")
        print(f"El area del rectangulo es de {area_rectangulo(valorBase, valorAltura)}")
        break
    except ValueError:
        system("cls")
        print("Error en la conversion: El valor ingresado no es un numero")

input("\nFin")