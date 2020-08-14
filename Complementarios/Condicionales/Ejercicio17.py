# Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de 
# las personas adultas de su sexo, siendo:
#       - estatura media de mujeres adultas: 1,65 m.
#       - estatura media de varones adultos: 1,72 m.

import OperacionesComunes as Operacion
from OperacionesComunes import tipo_de_numero as TipoNumero

altura = Operacion.solicitarNumero("Ingrese su altura en metros: ", soloPositivos = True, tipo = TipoNumero.Flotante)
Operacion.limpiarPantalla()

while(True):
    sexo = Operacion.solicitarCadena("¿M o F?: ", palabras_minimas = 1)
    Operacion.limpiarPantalla()
    if(sexo.lower() != "m" and sexo.lower() != "f"):
        print("Ingrese solo la inicial")
    else:
        break

if(sexo.lower() == "m"):
    print(f"La estatura media de varones adultos es: 1.72 m")
    print(f"Usted esta {'por encima de la media' if (altura > 1.72) else ('en la media' if (altura == 1.72) else 'por debajo de la media')}")
elif(sexo.lower() == "f"):
    print(f"La estatura media de mujeres adultas es: 1.65 m")
    print(f"Usted esta {'por encima de la media' if (altura > 1.65) else ('en la media' if (altura == 1.65) else 'por debajo de la media')}")

input("\nFin")