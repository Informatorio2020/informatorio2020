#Ejercicio 12:
# Escribí un programa que, dada una frase por el usuario, muestre la cantidad total de vocales
# (tanto mayúsculas como minúsculas) que contiene.

contador = 0
vocales = ["a", "e", "i", "o", "u"]

frase = input("Escriba una frase: ")

for actual in frase:
    if(actual.lower() in vocales):
        contador += 1

print(f"La frase tenia {contador} vocales")

input("\nFin")