# Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.

import OperacionesComunes as Operacion

respuesta = True
i = 0
menor = None

while(i < 3):
    if(menor == None):
        menor = Operacion.solicitarNumero("Ingrese el primer numero: ")
    else:
        aux = Operacion.solicitarNumero("Ingrese otro numero: ")

        if(aux < menor):
            respuesta = False
    
    i += 1

Operacion.limpiarPantalla()
print((f"{menor} fue el menor numero del conjunto") if (respuesta) else (f"{menor} no fue el menor numero del conjunto"))

input("\nFin")