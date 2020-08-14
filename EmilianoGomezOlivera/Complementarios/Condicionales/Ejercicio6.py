# Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del 
# salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:
#       Sueldo Actual (en $)        Aumento
#       0 – 6000					15%
#       6000 – 7900					10%
#       7900 – 12000				6%
#       Más de 12000				0%
# Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por 
# ciento de aumento, el sueldo actual y el sueldo aumentado.

import OperacionesComunes as Operacion

sueldo = Operacion.solicitarNumero("Ingrese el sueldo del jugador: $", soloPositivos = True)

if(sueldo <= 6000):
    print(f"A este jugador le corresponde un aumento del 15%, su nuevo sueldo seria ${Operacion.sumarPorcentaje(sueldo, 15)}")
elif(sueldo > 6000 and sueldo <= 7900):
    print(f"A este jugador le corresponde un aumento del 10%, su nuevo sueldo seria ${Operacion.sumarPorcentaje(sueldo, 10)}")
elif(sueldo > 7900 and sueldo <= 12000):
    print(f"A este jugador le corresponde un aumento del 6%, su nuevo sueldo seria ${Operacion.sumarPorcentaje(sueldo, 6)}")
else:
    print("A este jugador no le corresponde ningun aumento de sueldo")

input("\nFin")
