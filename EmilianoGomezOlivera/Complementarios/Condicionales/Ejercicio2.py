# Desarrolle un programa que permita determinar si un número X ingresado es par o impar.

import OperacionesComunes as Operacion

numero = Operacion.solicitarNumero(mensaje="Ingrese un numero: ")

print("Es par" if (Operacion.esPar(numero)) else "Es impar")

input("\nFin")