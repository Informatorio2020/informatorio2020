#Ejercicio 5:
# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas 
# ordenadas. La primera con los números pares y la segunda con los números impares.

import random

def separar(lista):
    pares = []
    impares = []

    for actual in lista:
        if(actual % 2 == 0):
            pares.append(actual)
        else:
            impares.append(actual)
    
    pares.sort()
    impares.sort()

    return (pares, impares)

numeros = []

for i in range(20):
    numeros.append(random.randint(0, 100))

listaPares, listaImpares = separar(numeros)

print("Lista de numeros pares")
print(listaPares)

print("\nLista de numeros impares")
print(listaImpares)

input("\nFin")