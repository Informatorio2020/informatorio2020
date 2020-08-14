#Ejercicio 6:
# Escribí un programa para solicitar al usuario el ingreso 
# de un número entero y que luego imprima si el número es 
# par o no. Recordar que un número es par si el resto, al 
# dividirlo por 2, es 0. 

from os import system

numero = None

# Bucle de control
while(True):
    if(numero == None):
        numero = input("Ingrese un numero: ")
        try:
            numero = int(numero)
            system("cls")
            print(f"{numero} es un numero par" if (numero % 2 == 0) else f"{numero} es un numero impar")
            break
        # Si el usuario ingresa un valor que no es un numero cae en la excepcion
        except ValueError:
            print(f"El valor ingresado '{numero}' es invalido: No se puede convertir a numero")
            # Se vuelve a setear la variable a None para reiniciar la operacion
            numero = None

input("Fin")