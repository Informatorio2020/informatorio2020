#Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo 
# que los reste y si no que los sume.

import OperacionesComunes as Operacion
from OperacionesComunes import tipo_de_numero

primerNumero = Operacion.solicitarNumero("Ingrese el segundo numero: ", tipo = tipo_de_numero.Flotante)
segundoNumero = Operacion.solicitarNumero("Ingrese el segundo numero: ", tipo = tipo_de_numero.Flotante)

if(primerNumero > segundoNumero):
    print(f"{primerNumero} - {segundoNumero} = {primerNumero - segundoNumero}")
else:
    print(f"{primerNumero} + {segundoNumero} = {primerNumero + segundoNumero}")

input("\nFin")