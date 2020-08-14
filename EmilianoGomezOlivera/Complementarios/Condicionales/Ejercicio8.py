# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de 
# ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10

import OperacionesComunes as Operacion

edad = Operacion.solicitarNumero("Ingrese su edad: ", soloPositivos = True)
print(f"Cada 10 segundos deberia tener {(220 - edad) / 10} pulsaciones")

input("\nFin")