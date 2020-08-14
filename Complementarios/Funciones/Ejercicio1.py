#Ejercicio 1: Triángulos
# Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo 
# rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando 
# el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que 
# lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su 
# función para calcular la longitud de la hipotenusa y muestre el resultado.

from math import sqrt
import OperacionesComunes as Operacion

def teorema(ladoA, ladoB):
    return round(sqrt((ladoA ** 2) + (ladoB ** 2)), 2)

ladoA = Operacion.solicitarNumero("Ingrese el valor de la base del triangulo: ", soloPositivos = True)
ladoB = Operacion.solicitarNumero("Ingrese el valor del segundo lado del triangulo: ", soloPositivos = True)

print(f"El valor de la hipotenusa es: {teorema(ladoA, ladoB)}")

input("\nFin")