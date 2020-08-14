#DESAFÍO 4
# Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño 
# indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6

i = 0

while(i < 6):
    if(i % 2 == 0):
        for x in range(0, 8):
            if(x % 2 == 0):
                print("V", end="\t")
            else:
                print("B", end="\t")
    else:
        for x in range(0, 8):
            if(x % 2 == 0):
                print("B", end="\t")
            else:
                print("V", end="\t")
    print("\n")
    i += 1

input("\n\nFin")