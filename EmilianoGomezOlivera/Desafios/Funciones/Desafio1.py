#Desafío 1
# 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede 
# tardar 1.000 años en desaparecer. 
# Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
# Un trozo de chicle tarda 5 años en degradarse. 
# Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, 
# botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.

from os import system

def degradado(material):
    if(material.lower() == "botella pet"):
        print("Una botella PET tarda 1000 años en degradarse")
    elif(material.lower() == "envase tetrabrik"):
        print("Un envase tetrabrik puede tardar hasta 30 años en degradarse")
    elif(material.lower() == "chicle"):
        print("Un pedazo de chicle tarda 5 años en degradarse")
    else:
        print("Error en la operacion. No se poseen los datos requeridos.")

while(True):
    degradado(input("Ingrese un material para conocer el tiempo que tarda en degradarse: "))
    opcion = input("\n¿Desea finalizar el programa? S/N (Por defecto No): ")

    if(opcion.lower() == "s" or opcion.lower() == "si"):
        break
    else:
        system("cls")

input("\nFin")