#Ejercicio 21:
# Escribí un programa que solicite al usuario una cadena de caracteres (que puede contener
# letras, números o símbolos). Analizar la cadena para mostrar: cuántas letras del abecedario
# (minúsculas y mayúsculas) contiene, cuántos símbolos (caracteres que no son ni letras ni
# números), cuántos dígitos numéricos y, de los dígitos, cuántos son múltiplos de 4.

import re
from os import system

# CADENA DE PRUEBA: #asd12dASD21ed40ac!"dsa"2831cAWe8

letras = None
numeros = None
especiales = None
multiplos = []

cadena = input("Ingrese una cadena de caracteres cualquiera: ")

especiales = cadena

# Uso expresiones regulares para matchear todas las coincidencias dentro del string y posteriormente las reemplazo
# Finalmente por descarte, debido al reemplazo, obtengo los caracteres especiales

letras = "".join(re.findall("[a-zA-Z]+", cadena))

for actual in (re.findall("[a-zA-Z]+", cadena)):
    print(actual)
    especiales = especiales.replace(actual, "")

numeros = "".join(re.findall("[0-9]+", cadena))

for actual in (re.findall("[0-9]+", cadena)):
    print(actual)
    especiales = especiales.replace(actual, "")

for actual in numeros:
    aux = int(actual)

    if(aux % 4 == 0):
        multiplos.append(actual)

system("cls")

print(f"Cadena ingresada: {cadena}")
print(f"Letras que componen la cadena: {letras}")
print(f"Numeros que componen la cadena: {numeros}")
print(f"Caracteres especiales que componen la cadena: {especiales}")
print(f"De los numeros, los multiplos de 4: {multiplos}")

input("\nFin")