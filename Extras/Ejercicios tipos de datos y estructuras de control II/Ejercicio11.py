#Ejercicio 11:
# Escribí un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto
# debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible
# por 400.

year = None

while(True):
    year = input("Ingrese un año: ")

    try:
        year = int(year)

        if(year < 0):
            print("La año ingresado no puede ser negativo")
        else:
            break
    except ValueError:
        print(f"Error en la converison de {year}: No es un numero")

if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("\nEl año ingresado es bisiesto")
else:
    print("\nEl año ingresado no es bisiesto")

input("\nFin")