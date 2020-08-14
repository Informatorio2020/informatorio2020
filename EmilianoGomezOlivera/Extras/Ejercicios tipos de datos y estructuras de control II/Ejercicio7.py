#Ejercicio 7:
# Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la
# cantidad de caracteres en la cadena es un número impar, o False si no lo es.

cadena = input("Escriba una frase: ")

print("\nLa cantidad de caracteres es impar" if (len(cadena) % 2 != 0) else "\nLa cantidad de caracteres es par")

input("\nFin")