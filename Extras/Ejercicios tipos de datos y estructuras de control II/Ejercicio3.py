#Ejercicio 3:
# Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el
# promedio de los tres.

from os import system

promedio = 0
i = 0

while(i < 3):
    numero = input("Ingrese un numero: ")

    try:
        numero = float(numero)
        promedio += numero
        i += 1
        system("cls")
    except ValueError:
        print(f"No se puede convertir '{numero}': No es un numero")

promedio = round(promedio / 3, 2)
print(f"El promedio de los tres numeros ingresados es: {promedio}")

input("\nFin")