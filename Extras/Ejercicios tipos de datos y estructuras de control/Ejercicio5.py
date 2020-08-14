#Ejercicio 5:
# Escribí un programa que solicite al usuario el ingreso de un texto 
# y almacene ese texto en una variable. A continuación, mostrar en 
# pantalla la primera letra del texto ingresado. Luego, solicitar 
# al usuario que ingrese un número positivo menor a la cantidad de 
# caracteres que tiene el texto que ingresó (por ejemplo, si escribió 
# la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar 
# este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.

from os import system

indice = None

# Mensaje que se utilizara para informar el rango numerico valido
mensaje = "Ingrese un numero entre 0 y {} inclusive: "

# Se solicita la cadena de caracteres que se utilizara
texto = input("Ingrese un texto: ")
print("La primera letra es: '", texto[0], "'")

# Bucle que se repite hasta que se ingrese un numero valido dentro del rango permitido (0, n)
while(True):
    # Lo primero es intentar obtener un numero valido
    if(indice == None):
        indice = input(mensaje.format((len(texto) - 1)))
        # Se intenta castear el dato de entrada
        try:
            indice = int(indice)
            system("cls")
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", indice, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            indice = None

    # Si se tiene un indice valido se finaliza el bucle
    else:
        break

print("Texto: ", texto)
print("El numero que ingreso corresponde al caracter '", texto[indice], "' del texto ya ingresado")
input("\nFin")