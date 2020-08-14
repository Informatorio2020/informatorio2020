#Ejercicio 13:
# Escribí un programa que muestre los primeros 10 números 
# de la sucesión de Fibonacci. La sucesión comienza con los 
# números 0 y 1 y, a partir de éstos, cada elemento es la 
# suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55… 

from os import system

actual = 0
siguiente = 1

for i in range (10):
    if(i == 0):
        print(i, end=", ")
        actual = 1
        print(actual, end=", ")
        print(siguiente, end=", ")        
    else:
        print(actual + siguiente, end=", ")
        aux = actual
        actual = siguiente
        siguiente += aux

input("Fin")