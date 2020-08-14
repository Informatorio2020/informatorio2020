#Desafío 1
# Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación
# del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 

from os import system

respuestas = []

while(True):
    valor = input("De la escala del 1 (Nada) al 10 (Estoy informado). \n¿Que tanto sabe sobre la contaminacion del medio ambiente?\nRespuesta: ")

    if(valor.isnumeric()):
        valor = int(valor)

        if(valor < 1 or valor > 10):
            system("cls")
            print("Respuesta invalida, debe ingresar un valor entre 1 y 10, puede incluir al 1 o al 10 en su respuesta")
        else:
            respuestas.append(valor)

            opcion = input("¿Agregar otra respuesta? S/N (Por defecto Si)")

            if(opcion.lower() == "n" or opcion.lower() == "no"):
                break
            else:
                system("cls")
    else:
        system("cls")
        print("La respuesta solo puede ser un valor numerico")

system("cls")
print("Las respuestas fueron: ")
respuestas.sort()
print(respuestas)

input("\nFin")