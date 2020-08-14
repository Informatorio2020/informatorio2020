# Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte 
# una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad 
# total invertida.

import OperacionesComunes as Operacion

monto = Operacion.solicitarNumero("Ingrese el dinero invertido: $", soloPositivos =True)

Operacion.limpiarPantalla()
primerSocio = Operacion.solicitarNumero("Ingrese el porcentaje aportado por el primer socio: ")

Operacion.limpiarPantalla()
segundoSocio = Operacion.solicitarNumero("Ingrese el porcentaje aportado por el segundo socio: ")

tercerSocio = 100 - (primerSocio + segundoSocio)

Operacion.limpiarPantalla()

print(f"El primer socio aporto un total de ${Operacion.obtenerPorcentaje(monto, primerSocio)}")
print(f"El segundo socio aporto un total de ${Operacion.obtenerPorcentaje(monto, segundoSocio)}")
print(f"El tercer socio aporto un total de ${Operacion.obtenerPorcentaje(monto, tercerSocio)}")

input("\nFin")