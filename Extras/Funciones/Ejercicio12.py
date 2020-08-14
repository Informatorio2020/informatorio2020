#Ejercicio 12:
# Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera 
# que las palabras están separadas por uno o más espacios. También podría haber espacios al principio 
# o al final del string pasado por parámetro. 

from os import system

def longitud(frase):
    resultado = frase.split(" ")

    return (resultado[-1], len(resultado[-1]))

frase = input("Ingrese una frase: ")

palabra, tamanho = longitud(frase)

print(f"La ultima palabra es '{palabra}' y tiene una longitud de {tamanho} caracteres")

input("\nFin")