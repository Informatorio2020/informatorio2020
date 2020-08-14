#Ejercicio 9:
# Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del 
# dígito en el número, utilizando para ello una función que calcule la frecuencia.

from os import system

def frecuencia(numero, digito):
    aux = numero
    i = 0

    if(numero == 0 and digito == numero):
        print("El digito aparece una vez en el numero ingresado")
    else:
        while(True):
            if(numero == 0):
                break

            if(numero % 10 == digito):
                i += 1
            
            numero = int(numero / 10)

        print(f"El digito [{digito}] aparaece {i} veces en el numero [{aux}]")

numero = int(input("Ingrese un numero: "))
digito = int(input("\nIngrese un digito: "))

frecuencia(numero, digito)

input("\nFin")