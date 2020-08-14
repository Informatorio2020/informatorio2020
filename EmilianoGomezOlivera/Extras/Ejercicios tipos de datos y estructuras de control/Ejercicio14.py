#Ejercicio 14:
# Escribí un programa que permita al usuario ingresar una 
# frase y luego un carácter (string de longitud 1) y luego 
# muestre la frase ingresada, pero con todas las ocurrencias 
# el carácter indicado por el usuario reemplazadas por “*”. 

from os import system

frase = None
caracter = None

# Bucle que controla que se haya ingresado los datos necesarios y validos
while(True):
    # Se solicita la frase al usuario
    if(frase == None):
        frase = input("Escriba una frase: ")
        # Se controla que la frase sea valida (al menos un caracter)
        if(frase == ""):
            print("Escriba una frase de al menos un caracter")
            frase = None
    # A continuacion se solicita un caracter
    elif(caracter == None):
        caracter = input("Ingrese un caracter: ")
        #Se valida el dato de entrada
        if(caracter == ""):
            print("Escriba un caracter valido")
            caracter = None
        elif(len(caracter) > 1):
            print(f"Usted ingreso '{caracter} pero solo se tendra en cuenta el primero")
            caracter = caracter[0]
    else:
        # Ya se poseen todos los datos necesarios y se procede a finalizar el bucle
        break

system("cls")
print(f"Frase ingresada: {frase}")
print(f"Caracter ingresado: {caracter}")
frase = frase.replace(caracter, "*")
print(f"Frase actualizada: {frase}")


input("Fin")