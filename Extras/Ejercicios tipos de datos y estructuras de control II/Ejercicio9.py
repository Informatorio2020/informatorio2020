#Ejercicio 9:
# Escribí un programa que, dado un número entero, muestre su valor absoluto. Recordá que,
# para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es
# 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el
# valor absoluto de -52 es 52).

numero = None

while(True):
    numero = input("Ingrese un numero: ")

    try:
        numero = int(numero)
        break
    except ValueError:
        print(f"Error en la converison de {numero}: No es un numero")

print("El valor absoluto es: ", numero if (numero >= 0) else (numero * -1))

input("\nFin")