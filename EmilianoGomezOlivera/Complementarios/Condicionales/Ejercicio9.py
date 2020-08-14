# En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El 
# presupuesto anual del hospital se reparte conforme a la sig. tabla:
#       ÁREA 		            PORCENTAJE
#       Pediatría		            60%
#       Traumatología		        20%
#       Kinesiología		        20%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.

import OperacionesComunes as Operacion

monto = Operacion.solicitarNumero("Ingrese el presupuesto anual: $", soloPositivos = True)

pediatria = Operacion.obtenerPorcentaje(monto, 60)
traumatologia = Operacion.obtenerPorcentaje(monto, 20)
kinesiologia = traumatologia

print(f"Al area de pediatria le corresponde ${pediatria}\nAl area de traumatologia le corresponde ${traumatologia}\nAl area de kinesiologia le corresponde ${kinesiologia}")

input("\nFin")