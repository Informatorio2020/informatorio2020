#Ejercicio 16:
# Escribí un programa que permita al usuario ingresar los montos de las compras de un
# cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada
# ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un
# monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al
# finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el monto
# total de 1000, se le debe aplicar un 10% de descuento.

from os import system

total = 0

while(True):
    aux = input("Ingrese un monto (0 para salir): $")

    if(aux == "0"):
        break
    else:
        try:
            aux = float(aux)
            if(aux < 0):
                print("El monto no puede ser menor a $0")
            else:
                total += aux
        except ValueError:
            print(f"Error en la converison de {aux}: No es un numero")
    
system("cls")

print(f"El precio final que debera pagar es: ${total if (total <= 1000) else (total * 0.9)}")

input("\nFin")