#Ejercicio 11:
# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si 
# no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

from os import system

def validar(dni):
    if(dni.isnumeric()):
        return (len(dni) == 7 or len(dni) == 8)
    else:
        return False

dni = input("Ingrese su DNI: ")

print(f"¿Es el DNI valido?: {validar(dni)}")

input("\nFin")