#Ejercicio 6:
# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es 
# válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene 
# el símbolo "@".

from os import system

def validar(correo):
    return ("@" in correo)

while(True):
    correo = input("Ingrese su correo: ")

    if(validar(correo)):
        system("cls")
        print(f"El correo '{correo}' es valido")
        break
    else:
        system("cls")
        print("El correo ingresado no es valido.")

input("\nFin")