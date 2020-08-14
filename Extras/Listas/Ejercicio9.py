#Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de
# veces que contiene cada vocal.

from os import system

vocales = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
palabra = None

while(True):
    palabra = input("Ingrese una palabra: ")

    if(len(palabra) < 2):
        print("Es necesario que ingrese al menos 2 letras")
    else:
        system("cls")
        break

for actual in palabra:
    if(actual.lower() == "a"):
        vocales["A"] += 1
    elif(actual.lower() == "e"):
        vocales["E"] += 1
    elif(actual.lower() == "i"):
        vocales["I"] += 1
    elif(actual.lower() == "o"):
        vocales["O"] += 1
    elif(actual.lower() == "u"):
        vocales["U"] += 1

print(f"Usted ingreso la palabra '{palabra}'\n\nLa palabra ingresada tiene la siguiente cantidad de vocales:")
for actual in vocales:
    print(f"\n{actual}: {vocales.get(actual)} veces")
input("\nFin")