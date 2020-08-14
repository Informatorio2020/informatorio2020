#Ejercicio 7:
# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus 
# dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus 
# dígitos. Utilizando una función que realice dichas sumatorias.

from os import system

def sumatoria(lista):
    resultado = 0

    for actual in lista:
        resultado += actual

    return resultado

def sumarDigitos(numero):
    resultado = 0

    while(True):
        if(numero == 0):
            break
        else:
            resultado += (numero % 10)
            numero = int(numero / 10)
    
    return resultado

numeros = []

while(True):
    valor = input("\nIngrese un numero (0 para finalizar): ")

    if(valor == "0"):
        break
    else:
        if(valor.isnumeric()):
            valor = int(valor)
            print(f"La sumatoria de los digitos de {valor} es: {sumarDigitos(valor)}")
            numeros.append(valor)
        else:
            print(f"Error en la conversion de '{valor}': No es un numero")

resultadoFinal = sumatoria(numeros)
print(f"\n\nLa sumatoria de todos los numeros ingresados es: {resultadoFinal}")
print(f"La sumatoria de los digitos de {resultadoFinal} es: {sumarDigitos(resultadoFinal)}")

input("\nFin")