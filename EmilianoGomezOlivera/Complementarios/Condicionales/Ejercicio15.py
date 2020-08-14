#Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
#     i. Si trabaja 40 horas o menos se le paga $16 por hora
#     ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.

import OperacionesComunes as Operacion

horas = Operacion.solicitarNumero("Ingrese la cantidad de horas que trabaja: ", soloPositivos = True)

if(horas <= 40):
    print(f"El sueldo correspondiente es: ${horas * 16}")
else:
    print(f"El sueldo correspondiente es: ${(40 * 16) + ((horas - 40) * 20)}")

input("\nFin")