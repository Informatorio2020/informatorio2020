#Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por
# pantalla en orden inverso separados por comas.

lista = []

print("Lista original de numeros: ")
for i in range(1, 11):
    print(i, end=", ")
    lista.append(i)

print("\n\nLista invertida de numeros: ")
lista.reverse()
for actual in lista:
    print(actual, end=", ")

input("\n\nFin")