#DESAFÍO 3
# En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra 
# llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la 
# caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar 
# la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 
# 
# Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 
# 25% y si es blanca no obtendrá descuento.

from os import system

while(True):
    monto = input("Ingrese el monto a pagar: $")

    try:
        monto = float(monto)

        if(monto > 0):
            opcion = input("\n¿Que codigo de descuento aplica?\nB - Sin descuento\nA - 25% de descuento\nR - 40% de descuento\nOpcion: ")

            system("cls")
            print(f"Monto original a pagar: ${monto}")
            if(opcion.lower() == "a"):            
                print(f"Monto con descuento aplicado: ${monto * 0.75}")
            elif(opcion.lower() == "r"):            
                print(f"Monto con descuento aplicado: ${monto * 0.60}")
            else:
                print("No se aplica ningun descuento, debe pagar el monto original")

            opcion = input("\n¿Registrar otra transaccion? S/N (Por defecto Si): ")

            if(opcion.lower() == "n" or opcion.lower() == "no"):
                break
            else:
                system("cls")
        else:
            print("Error en la operacion: El monto ingresado no puede ser menor a 0")

    except ValueError:
        print(f"Error en la conversion de '{monto}'': No es un numero")

input("\nFin")