# Ejercicio13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una 
# lista y muestre por pantalla su media y desviación típica

import OperacionesComunes as Operacion
from OperacionesComunes import tipo_de_numero as Numero
from math import sqrt

valores = []
acumulador = 0
media = None
varianza = None

while(True):
    valores.append(Operacion.solicitarNumero("Ingrese un numero: ", tipo=Numero.Flotante))

    if(Operacion.Si_No()):
        Operacion.limpiarPantalla()        
    else:
        Operacion.limpiarPantalla()
        break

for actual in valores:
    acumulador += actual

media = round((acumulador / len(valores)), 2)

acumulador = 0

for actual in valores:
    acumulador += (actual - media) ** 2

varianza = round((acumulador / (len(valores) - 1)), 2)

print(f"La media es: {media}")
print(f"La varianza es: {varianza}")
print(f"La desviacion tipica es: {round(sqrt(varianza), 2)}")

input("\nFin")