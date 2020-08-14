#Desafío 4
# Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el 
# mensaje Hola soy ......, cuidame.
# Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior 
# para los n nombres que se encuentran a partir de la posición i.

from os import system

setAuxiliar = set()
animales = None
numero = None
cantidad = None

while(True):
    if(animales == None):
        animal = input("Ingrese el nombre de un animal: ")
        setAuxiliar.add(animal)

        opcion = input("¿Desea agregar otro animal? S/N (Por defecto Si)")

        if(opcion.lower() == "s" or opcion.lower() == "si"):
            system("cls")
        else:
            animales = tuple(setAuxiliar)
            system("cls")
    elif(numero == None):
        valor = input(f"Ingrese un numero del 1 al {len(animales)}: ")

        if(valor.isnumeric()):
            numero = int(valor)

            if(numero < 1 or numero > len(animales)):
                system("cls")
                print("Debe ingresar un numero entre el rango dado")
            else:
                cantidad = input(f"Ingrese la cantidad de animales que se mostrara: ")

                if(cantidad.isnumeric()):
                    numero -= 1
                    aux = int(cantidad)
                    cantidad = (numero + aux) if ((numero + aux) < len(animales)) else len(animales) 
                else:
                    system("cls")
                    print(f"No se puede convertir '{cantidad}': No es un numero")
        else:
            system("cls")
            print(f"No se puede convertir '{cantidad}': No es un numero")
    else:
        break

for i in range(numero, cantidad):
    print(f"Hola soy {animales[i]}, cuidame.")


input()