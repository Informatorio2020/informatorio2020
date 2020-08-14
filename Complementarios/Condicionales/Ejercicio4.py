# Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m

import OperacionesComunes as Operacion

variableM = Operacion.solicitarNumero("Ingrese el primer numero: ")
variableN = Operacion.solicitarNumero("Ingrese el segundo numero: ")

print(f"{variableN} es divisor de {variableM}" if (variableM % variableN) else f"{variableN} es divisor de {variableM}")

input("\nFin")