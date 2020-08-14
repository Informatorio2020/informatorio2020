#Ejercicio 1:
# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo
# en una variable. A continuación, el programa debe solicitar al usuario que ingrese un
# número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el
# resultado de la suma de los dos números ingresados por el usuario. Por último, se debe
# mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se
# reemplazará por el resultado de la operación.

from os import system

nroDecimal = None
nroEntero = None
suma = None

# Bucle que se repite hasta que se ingrese un numero valido para ambas variables
while(True):
    # Lo primero es intentar obtener un numero que se pueda convertir en float
    if(nroDecimal == None):
        nroDecimal = input("Ingrese un numero con decimales: ")
        # Se intenta castear el dato de entrada
        try:
            nroDecimal = float(nroDecimal)
            system("cls")
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", nroDecimal, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            nroDecimal = None

    # A continuacion se solicita un numero entero
    elif(nroEntero == None):
        nroEntero = input("Ingrese un numero entero: ")
        # Se vuelve a intentar castear el dato de entrada
        try:
            nroEntero = int(nroEntero)
            system("cls")
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:            
            print("'", nroEntero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            nroEntero = None

    # Si se tienen ambos numeros se finaliza el bucle
    else:
        break

suma = nroDecimal + nroEntero
print("El primer numero ingresado fue: ", nroDecimal)
print("El segundo numero ingresado fue: ", nroEntero)
print("El resultado de la suma es ", suma)
input("\nFin")