#Ejercicio 3: Calculadora de envío
# Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y 
# $2.95 para cada segundo elemento posterior. Escriba una función que tome el número de elementos en 
# el pedido como su único parámetro. Devuelva los gastos de envío del pedido como resultado de la 
# función. Incluya un programa principal que lea la cantidad de artículos comprados al usuario y 
# muestre los gastos de envío.

import OperacionesComunes as Operacion

PRIMER_ELEMENTO = 10.95
SIGUIENTES_ELEMENTOS = 2.95

def calculadoraEnvios(paquetes):
    if(paquetes == 0):
        return 0
    else:
        acumulado = PRIMER_ELEMENTO
        paquetes -= 1
        acumulado += (paquetes * SIGUIENTES_ELEMENTOS)

        return round(acumulado, 2)

paquetes = Operacion.solicitarNumero("Ingrese el numero de envios a realizar: ", soloPositivos = True)

print(f"El total del costo de envio sera: ${calculadoraEnvios(paquetes)}")

input("\nFin")