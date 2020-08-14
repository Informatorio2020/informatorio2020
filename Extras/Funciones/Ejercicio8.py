#Ejercicio 8:
# Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una 
# función booleana que lo decida.

from os import system

def primo(numero):
    i = 1
    esPrimo = True

    for x in range(2, (numero + 1)):
        if(numero % x == 0):
            i += 1
            
        if(i == 3):
            esPrimo = False
            break
        

    return esPrimo
        
numero = int(input("Ingrese un numero: "))

print("\nEs primo" if (primo(numero)) else "\nNo es primo")

input("\nFin")