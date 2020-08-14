#Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres 
# camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de 
# tres camisas un descuento del 10%.

import OperacionesComunes as Operacion
from OperacionesComunes import tipo_de_numero

cantidad = Operacion.solicitarNumero("¿Cuantas camisas esta comprando?: ", soloPositivos = True)
Operacion.limpiarPantalla()

monto = Operacion.solicitarNumero("Ingrese el monto a pagar: $", soloPositivos = True, tipo = tipo_de_numero.Flotante)
Operacion.limpiarPantalla()

print(f"Cantidad de camisas: {cantidad} unidades.\nPrecio: ${monto}")

if(cantidad >= 3):
    print(f"Descuento: 20%.\nPrecio con descuento: ${Operacion.obtenerPorcentaje(monto, 80)}")
else:
    print(f"Descuento: 10%.\nPrecio con descuento: ${Operacion.obtenerPorcentaje(monto, 90)}")

input("\nFin")