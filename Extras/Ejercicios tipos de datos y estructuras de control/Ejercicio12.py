#Ejercicio 12:
# Escribí un programa que, dado un número por el usuario, 
# muestre todos sus divisores positivos. Recordá que un 
# divisor es aquel que divide al número de forma exacta 
# (con resto 0).

from os import system

numero = None
fin = None
divisores = []

# Bucle de control
while(True):
    if(numero == None):
        numero = input("Ingrese un numero: ")
        try:
            numero = int(numero)
            system("cls")
            break
        # Si el usuario ingresa un valor que no es un numero cae en la excepcion
        except ValueError:
            print(f"El valor ingresado '{numero}' es invalido: No se puede convertir a numero")
            # Se vuelve a setear la variable a None para reiniciar la operacion
            numero = None

fin = numero if (numero >= 0) else (numero * -1)

for i in range(1, fin + 1):
    if(numero % i == 0):
        divisores.append(i)

print(f"Los divisores de {numero} son: {divisores}")

input("Fin")