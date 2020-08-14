#Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

from os import system

lista = []

while(True):
    numero = input("Ingrese uno de los numeros ganadores: ")

    try:
        numero = int(numero)
        lista.append(numero)
        
        opcion = input("¿Continuar? S/N: ")
        if(opcion.lower() == "n"):            
            system("cls")
            break
        else:
            system("cls")
    except ValueError:
        print(f"No se puede convertir '{numero}': No es un numero")

lista.sort()

print("Los numeros ganadores son: ", end="")
for actual in lista:
    print(actual, end=", ")

input("\nFin")