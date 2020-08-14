#Ejercicio 5:
# Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto
# en el último año y almacene ese número en una variable. A continuación mostrar en
# pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3
# shows.

from os import system

shows = None

while(True):
    numero = input("¿Cuantos shows ha visto?: ")

    try:
        numero = int(numero)

        if(numero < 0):
            print("No puede haber visto menos de 0 shows")
        else:
            shows = numero
            break
    except ValueError:
        print(f"Error en la conversion de '{numero}': No es un numero")

system("cls")
print("Usted ha visto mas de 3 shows" if (shows > 3) else "Usted no ha visto mas de 3 shows")

input("\nFin")