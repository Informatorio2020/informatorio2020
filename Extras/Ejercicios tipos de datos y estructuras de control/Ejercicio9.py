#Ejercicio 9:
# Escribí un programa que solicite al usuario una letra 
# y, si es una vocal, muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un 
# carácter y, en ese caso, informarle que no se puede procesar el dato. 

from os import system

# Se guardan las vocales una lista porque ya se conocen esos datos
vocales = ["a", "e", "i", "o", "u"]
letra = None

# Bucle de control
while(True):
    # Se solicita si al usuario una letra si no existiese una ya asignada
    if(letra == None):
        letra = input("Ingrese una letra: ")

        if(len(letra) > 1 or letra == ""):
            print("No se puede procesar el dato de entrada, ingrese solo una letra")
            letra = None
        else:
            break

system("cls")
print(f"'{letra}' es una vocal" if (letra.lower() in vocales) else f"'{letra}' no es una vocal")

input("Fin")