#Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

from os import system

caracter = "a"
lista = []

for i in range(26):
    lista.append(caracter)
    if(caracter == "n"):
        lista.append("ñ")

    caracter = chr(ord(caracter) + 1)

system("cls")
print("Abecedario: ")

for actual in lista:
    print(actual, end=" ")

print("\n\nLetras en posiciones multiples de 3: ")

for i in range(len(lista)):
    if(i % 3 == 0):
        print(lista[i], end=" ")

input("\n\nFin")
