#Ejercicio 17:
# Escribí un programa que permita al usuario ingresar una cantidad de números positivos
# indefinida (la cantidad que ingresará no se conoce y puede cambiar en cada ejecución),
# finalizando cuando ingresa el número 0 (que no se tendrá en cuenta). Una vez terminada la
# lectura de números, informar cuál fue el mayor de los números ingresados.

from os import system

mayor = None

while(True):
    if(mayor == None):
        aux = input("Ingrese un numero: ")

        if(aux == "0"):
            mayor = 0
            break
        else:
            try:
                aux = float(aux)
                mayor = aux
            except ValueError:
                print(f"Error en la converison de {aux}: No es un numero")
    else:
        aux = input("Ingrese otro numero: ")
        if(aux == "0"):
            break
        else:
            try:
                aux = float(aux)
                mayor = aux if (aux > mayor) else mayor
            except ValueError:
                print(f"Error en la converison de {aux}: No es un numero") 

system("cls")
print(f"El mayor numero fue: {mayor}")


input("\nFin")