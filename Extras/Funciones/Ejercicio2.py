#Ejercicio 2:
# Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un 
# radio. Calcula el área de un círculo de 5 de radio:

from os import system

def area_circulo(radio):
    return round((3.14 * (radio ** 2)), 2)

print(f"El area de un circulo con un radio de 5 es: {area_circulo(5)}")

input("\nFin")