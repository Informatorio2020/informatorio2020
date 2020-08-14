# Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
# Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento 
# obtenido, si es que corresponde.

import OperacionesComunes as Operacion

monto = Operacion.solicitarNumero("Ingrese el monto a pagar: $", soloPositivos = True)

if(monto > 1000):
    monto = Operacion.obtenerPorcentaje(monto, 85)

print(f"Debera pagar ${monto}", ", el monto a pagar ya refleja un descuento del 15%." if (monto > 1000) else ".")

input("\nFin")