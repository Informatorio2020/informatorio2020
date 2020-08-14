#Ejercicio 2:
# Escribí un programa que solicite al usuario dos números y 
# los almacene en dos variables. En otra variable, almacená 
# el resultado de la suma de esos dos números y luego mostrá 
# ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que 
# ingrese un tercer número, el cual se debe almacenar en una 
# nueva variable. Por último, mostrá en pantalla el resultado 
# de la multiplicación de este nuevo número por el resultado 
# de la suma anterior. 

from os import system

primerNumero = None
segundoNumero = None
tercerNumero = None
suma = None
multiplicacion = None

# Bucle que se repite hasta que se ingrese un numero valido para todas las variables
while(True):
    # Se solicita el primer numero
    if(primerNumero == None):
        primerNumero = input("Ingrese el primer numero: ")
        # Se intenta castear el dato de entrada
        try:
            primerNumero = int(primerNumero)
            system("cls")
            # Se asigna el primer dato de la suma
            suma = primerNumero
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", primerNumero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            primerNumero = None

    # A continuacion se solicita el segundo numero
    elif(segundoNumero == None):
        segundoNumero = input("Ingrese el segundo numero: ")
        # Se vuelve a intentar castear el dato de entrada
        try:
            segundoNumero = int(segundoNumero)
            system("cls")
            # Debido a que se tienen todos los datos necesarios es posible realizar la suma
            suma += segundoNumero
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:            
            print("'", segundoNumero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            segundoNumero = None

    # Finalmente se pide el tercer numero
    elif(tercerNumero == None):
        tercerNumero = input("Ingrese el tercer numero: ")
        # Se vuelve a intentar castear el dato de entrada
        try:
            tercerNumero = int(tercerNumero)
            system("cls")
            # Se realiza la multiplicacion solicitada
            multiplicacion = tercerNumero * suma
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:            
            print("'", tercerNumero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            tercerNumero = None

    # Si se tienen todos los numeros se finaliza el bucle
    else:
        break

print("El resultado de la suma entre ", primerNumero, " y ", segundoNumero, " es igual a ", suma)
print("El resultado de la multiplicacion entre ", suma, " y ", tercerNumero, " es igual a ", multiplicacion)
input("\nFin")