# Leer una frase y luego invierta el orden de las palabras en la frase. 
# Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.

from os import system

frase = None
inverso = None

frase = input("Ingrese una frase: ")
            
inverso = frase.split(" ")
inverso = inverso[::-1]

print(f"Frase ingresada: '{frase}'")
frase = ""

for actual in inverso:
    frase += actual + " "

print(f"Frase invertida: '{frase}'")

input("\nFin")