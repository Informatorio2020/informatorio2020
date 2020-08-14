#Ejercicio 2:
# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por
# una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido.
# Mostrar el consumo de combustible por kilómetro.

from os import system

km = None
litros = None
consumo = None

while(True):
    if(km == None):
        km = input("Ingrese la cantidad de kilometros recorridos: ")

        try:
            km = float(km)
            system("cls")
        except ValueError:
            print(f"No se puede convertir '{km}': No es un numero")
            km = None
    elif(litros == None):
        litros = input("Ingrese la cantidad de litros de combustible consumidos: ")

        try:
            litros = float(litros)
            system("cls")
        except:
            print(f"No se puede convertir '{litros}': No es un numero")
            litros = None
    else:
        break

print(f"Distancia recorrida: {km} km")
print(f"Combustible consumido: {litros} l")

consumo = round(((1 * litros) / km), 2)
print(f"Consumo por kilometro: {consumo} l")

input("\nFin")