#Hacer un programa que imprima el nombre de un artículo, clave, precio original y su 
# precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 el 
# descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).

import OperacionesComunes as Operacion

articulo = Operacion.solicitarCadena("Ingrese el nombre del articulo: ", palabras_minimas = 1)
Operacion.limpiarPantalla()

precio = Operacion.solicitarNumero("Ingrese el precio del articulo: $", soloPositivos = True)
Operacion.limpiarPantalla()

codigo = Operacion.solicitarCadena("Ingrese el codigo de descuento: ", palabras_minimas = 1)
Operacion.limpiarPantalla()

print(f"Articulo: {articulo}.\nPrecio: ${precio}.")

if(codigo == "01"):
    print(f"Descuento: 10%\nPrecio con descuento: ${Operacion.obtenerPorcentaje(precio, 90)}")
elif(codigo == "02"):
    print(f"Descuento: 20%\nPrecio con descuento: ${Operacion.obtenerPorcentaje(precio, 80)}")
else:
    print(f"Descuento: 0%\nPrecio con descuento: ${precio}")

input("\nFin")