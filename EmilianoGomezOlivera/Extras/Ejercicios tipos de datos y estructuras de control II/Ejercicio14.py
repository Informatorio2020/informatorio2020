#Ejercicio 14:
# Escribí un programa que permita al usuario ingresar 6 números enteros, que pueden ser
# positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el
# promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es
# necesario evitar que el programa arroje un error si no se ingresaron números positivos.

from os import system

numeros = []
sumatoria = 0
promedio = 0
cantidad = 0
i = 0

while(i < 6):
    numero = input("Ingrese un numero: ")

    try:
        numero = float(numero)
        numeros.append(numero)
        i += 1
    except ValueError:
        print(f"Error en la converison de {numero}: No es un numero")

for actual in numeros:
    if(actual >= 0):
        promedio += actual
        cantidad += 1
    else:
        sumatoria += actual

promedio = 0 if (cantidad == 0) else (promedio / cantidad)

system("cls")

print(f"Promedio de positivos: {promedio}\nSumatoria de negativos: {sumatoria}")

input()