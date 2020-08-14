#Ejercicio 6:
# Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números,
# donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el
# año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero).
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.

from os import system

fecha = None
year = None
mes = None
dia = None

while(True):
    fecha = input("Ingrese una fecha (DDMMAAAA): ")

    try:
        fecha = int(fecha)

        if(fecha < 0):
            print("La fecha ingresada no puede ser negativa")
        else:
            break
    except ValueError:
        print(f"Error en la converison de {fecha}: No es un numero")

year = int(fecha % 10000)
fecha /= 10000
mes = int(fecha % 100)
fecha /= 100
dia = int(fecha)

system("cls") 

print("La fecha ingresada fue: ", dia, "/", ("0" + str(mes) if mes < 10 else mes), "/", year)

input("\nFin")