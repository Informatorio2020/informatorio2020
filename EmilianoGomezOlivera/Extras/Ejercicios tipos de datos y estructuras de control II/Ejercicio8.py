#Ejercicio 8:
# Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos
# variables, y que luego imprima True si la primera palabra es menor que la segunda o False
# si no lo es.

palabraA = input("Escriba una palabra: ")
palabraB = input("Escriba otra palabra: ")

print("La primera palaba no tiene mas letras que la segunda palabra" if len(palabraA) < len(palabraB) else "La primera palabra tiene mas letras")

input("\nFin")