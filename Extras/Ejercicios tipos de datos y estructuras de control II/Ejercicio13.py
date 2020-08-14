#Ejercicio 13:
# Escribí un programa que, dado un número entero positivo, calcule y muestre su factorial. El
# factorial de un número se obtiene multiplicando todos los números enteros positivos que hay
# entre el 1 y ese número. El factorial de 0 es 1.

numero = None
factorial = 1

while(True):
    numero = input("Ingrese un numero natural: ")

    try:
        numero = int(numero)

        if(numero < 0):
            print("El numero ingresado no puede ser negativo")
        else:
            break
    except ValueError:
        print(f"Error en la converison de {numero}: No es un numero")

if(numero == 0 or numero == 1):
    factorial = 1
else:
    for i in range(1, numero + 1):
        factorial *= i

print(f"El factorial es: {factorial}")

input("\nFin")