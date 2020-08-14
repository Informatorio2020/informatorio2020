#Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
# palíndromo.

from os import system

palabra = None
inverso = None
noPalindromo = False

while(True):
    palabra = input("Ingrese una palabra: ")

    if(len(palabra) < 2):
        print("Es necesario que ingrese al menos 2 letras")
    else:
        break

# Se invierte el sentido de la palabra
inverso = palabra[::-1]

for i in range(len(palabra)):
    if(palabra[i].lower() != inverso[i].lower()):
        noPalindromo = True
        break

print(f"{palabra} no es un palindromo" if (noPalindromo) else f"{palabra} es un palindromo")

input("\nFin")