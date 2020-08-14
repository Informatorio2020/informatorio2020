#Ejercicio 19:
# Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo
# carácter), uno por vez. La repetición finalizará cuando se ingrese un string que no tenga
# longitud 1, o cuando el string ingresado corresponda al dígito numérico 0. Al finalizar,
# mostrar el string completo que se formó con todos los caracteres ingresados y qué
# porcentaje de caracteres del total fueron la letra “a”.

from os import system

palabra = []
letrasA = 0

while(True):
    caracter = input("Ingrese un caracter (0 para salir o mas de un caracter): ")

    if(len(caracter) > 1 or caracter == "0"):
        break
    else:
        palabra.append(caracter)

system("cls")

print("Palabra ingresada: ", end="")
for actual in palabra:
    if(actual.lower() == "a"):
        letrasA += 1
    
    print(actual, end="")

print(f"\nSe ingresaron {letrasA} letras 'A', equivalente a un {(letrasA / len(palabra) * 100)}% del total de la oracion")

input("\nFin")