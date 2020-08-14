#Ejercicio 20:
# Escribí un programa que, dado un número entero por el usuario (guardado como int),
# muestre la suma de todos sus dígitos. Recordá que vas a necesitar obtener cada uno de los
# dígitos por separado para poder sumarlos entre sí.

numero = None
sumatoria = 0

while(True):
    numero = input("Ingrese un numero entero: ")

    try:
        numero = int(numero)
        break
    except ValueError:
        print(f"Error en la converison de {numero}: No es un numero")

aux = numero if (numero > 0) else (numero * -1)

while(True):
    if(aux == 0):
        break
    else:
        sumatoria += (aux % 10)
        aux = int(aux / 10)

print(f"La sumatoria de los digitos es: {sumatoria}")

input("\nFin")