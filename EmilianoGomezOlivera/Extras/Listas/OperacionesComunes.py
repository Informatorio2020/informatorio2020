from enum import Enum
from os import system

# Autor: Gómez Olivera, Emiliano (Comision 4)
# Fecha: 28/06/2020
# Hora: 2:54
# Version: 0.2 
# ¯\_(ツ)_/¯

# Una enumeracion, why not?
class tipo_de_numero(Enum):
    Entero = 1
    Flotante = 2

# Funcion para solicitar un numero al usuario, se puede definir un mensaje propio o usar predeterminado
# Se puede cambiar el tipo de dato al que convertir si se setea el parametro 'tipo' a:
#       - tipo_de_numero.Entero (Un numero entero positivo o negativo)
#       - tipo_de_numero.Flotante (Un numero con decimales positivo o negativo)
# Ahora se puede setear si aceptara numeros negativos o no con el parametro 'soloPositivos' (Por defecto en False)
def solicitarNumero(mensaje = "Ingrese un numero: ", tipo = tipo_de_numero.Entero, soloPositivos = False):
    valor = None
    while(True):
        if(valor == None):
            valor = input(mensaje)

            try:
                if(tipo == tipo_de_numero.Entero):
                    valor = int(valor)
                else:
                    valor = float(valor)

                if(soloPositivos and valor < 0):
                    valor = None
                    system("cls")
                    print("El numero que se ingresa no puede ser negativo")
            except:
                system("cls")
                print(f"Error en la conversion de '{valor}': No es un numero")
                valor = None
        else:
            return valor

# Solicita al usuario una cadena de caracteres, se le puede setear un mensaje si es necesario
# Ademas, se le puede establecer un minimo de palabras para que la cadena sea valida
def solicitarCadena(mensaje = "Ingrese una cadena de texto: ", palabras_minimas = 2):
    valor = None
    while(True):
        valor = input(mensaje)

        if(len(valor.split(" ")) < palabras_minimas):
            system("cls")
            print(f"El texto debe contener al menos {palabras_minimas} palabras separadas por espacios.")
            valor = None
        else:
            return valor

# Mensaje de confirmacion para saber si finalizar un programa o no
# Devuelve un booleano que puede se utilizado en un if/elif.
def Si_No(mensaje = "¿Desea finalizar? S/N (Por defecto No): "):
    respuesta = input(mensaje)

    return True if (respuesta.lower() == "s" or respuesta.lower() == "si") else False

# Procedimiento para limpiar la pantalla porque me cansaba tener que estar importando el mismo script 
# todo el tiempo :P
def limpiarPantalla():
    system("cls")

# Funcion para saber si un numero es par o impar, por que no?
def esPar(numero):
    return ((numero % 2) == 0)

# Funcion que suma todos los digitos que componen un numero
def sumarDigitos(numero):
    aux = numero
    acumulador = 0

    while(aux != 0):
        acumulador += aux % 10
        aux = int(aux/10)
    
    return acumulador

# Funcion para obtener el porcentaje de un numero
def obtenerPorcentaje(numero, porcentaje):
    aux = (porcentaje / 100)
    
    return round(numero * aux, 2)

# Funcion para sumar un porcentaje a un numero
def sumarPorcentaje(numero, porcentaje):
    aux = (porcentaje / 100) + 1
    
    return round(numero * aux, 2)