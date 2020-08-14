#Ejercicio 10:
# Escribí un programa que solicite al usuario el ingreso de 10 números diferentes y muestre
# en pantalla al mayor de ellos.

from os import system

mayor = None
i = 0

while(i < 10):
    if(mayor == None):
        aux = input("Ingrese un numero: ")
        try:
            aux = float(aux)
            mayor = aux
            i += 1
        except ValueError:
            print(f"Error en la converison de {aux}: No es un numero")

    else:
        aux = input("Ingrese otro numero: ")
        try:
            aux = float(aux)
            mayor = aux if (aux > mayor) else mayor
            i += 1
        except ValueError:
            print(f"Error en la converison de {aux}: No es un numero")    

system("cls")
print(f"El mayor numero fue: {mayor}")


input("\nFin")