#Ejercicio 4:
# Escribí un programa que solicite al usuario 5 números, sumarlos, calcular el promedio e
# informar cuanto es el 15% de esa suma, almacenar cada resultado en una variable.
# Calcular, además, el promedio de los números ingresados.. A continuación, mostrar el
# resultado final de cada cálculo en pantalla.

from os import system

promedio = None
porcentaje = None
sumatoria = 0
i = 0

while(i < 5):
    numero = input("Ingrese un numero: ")

    try:
        numero = float(numero)
        sumatoria += numero
        i += 1
        system("cls")
    except ValueError:
        print(f"No se puede convertir '{numero}': No es un numero")

promedio = round(sumatoria / 5, 2)
porcentaje = sumatoria * 0.15

print(f"La sumatoria de los numeros ingresados es: {sumatoria}")
print(f"El promedio es: {promedio}")
print(f"El 15% de la sumatoria es: {porcentaje}")

input("\nFin")