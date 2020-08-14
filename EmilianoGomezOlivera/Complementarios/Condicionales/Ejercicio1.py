# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

import OperacionesComunes as Operacion

valorA = Operacion.solicitarNumero("Ingrese el primer numero: ")
valorB = Operacion.solicitarNumero("Ingrese el segundo numero: ")
valorC = Operacion.solicitarNumero("Ingrese el tercer numero: ")

if(valorA > valorB and valorA > valorC):
    print(valorA)
    if(valorB > valorC):
        print(valorB, "\n", valorC)
    else:
        print(valorC, "\n", valorB)
elif(valorB > valorC):
    print(valorB)
    if(valorA > valorC):
        print(valorA, "\n", valorC)
    else:
        print(valorC, "\n", valorA)
else:
    print(valorC)
    if(valorA > valorB):
        print(valorA, "\n", valorB)
    else:
        print(valorB, "\n", valorA)

input("\nFin")