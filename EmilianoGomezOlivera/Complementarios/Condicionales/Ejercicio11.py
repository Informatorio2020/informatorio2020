#Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio 
# de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.

import OperacionesComunes as Operacion

promedio = Operacion.solicitarNumero("Ingrese la primera nota: ", soloPositivos = True)
promedio += Operacion.solicitarNumero("Ingrese la segunda nota: ", soloPositivos = True)
promedio += Operacion.solicitarNumero("Ingrese la tercera nota: ", soloPositivos = True)
promedio /= 3

if(promedio):
    print(f"\nEl alumno ha aprobado. Promedio: {round(promedio, 2)}.")
else:
    print(f"\nEl alumno ha desaprobado. Promedio: {round(promedio, 2)}.")

input("\nFin")