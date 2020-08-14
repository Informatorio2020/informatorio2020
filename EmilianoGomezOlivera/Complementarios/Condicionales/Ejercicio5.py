#Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine 
# qué tipo de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor 
# de los tres lados y B y C corresponden con los otros dos, entonces:
#       Si A>=B + C à No se trata de un triángulo
#       Si A2 = B2 + C2 à Es un triángulo rectángulo
#       Si A2 > B2 + C2 à Es un triángulo obtusángulo
#       Si A2 < B2 + C2 à Es un triángulo acutángulo

import OperacionesComunes as Operacion
from OperacionesComunes import tipo_de_numero as Tipo

ladoA = Operacion.solicitarNumero("Ingrese el primer lado: ", soloPositivos = True, tipo = Tipo.Flotante)
ladoB = Operacion.solicitarNumero("Ingrese el segundo lado: ", soloPositivos = True, tipo = Tipo.Flotante)
ladoC = Operacion.solicitarNumero("Ingrese el tercer lado: ", soloPositivos = True, tipo = Tipo.Flotante)

if(ladoA >= (ladoB + ladoC)):
    print("No es un triangulo")
elif(ladoA ** 2 == ladoB ** 2 + ladoC ** 2):
    print("Es un triangulo rectangulo")
elif(ladoA ** 2 > ladoB ** 2 + ladoC ** 2):
    print("Es un triangulo obtusángulo")
elif(ladoA ** 2 < ladoB ** 2 + ladoC ** 2):
    print("Es un triangulo acutángulo")

input("\nFin")