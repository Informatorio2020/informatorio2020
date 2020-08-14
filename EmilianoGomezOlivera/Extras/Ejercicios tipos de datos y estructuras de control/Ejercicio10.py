#Ejercicio 10:
# Escribí un programa para solicitar al usuario tres 
# números y mostrar en pantalla al menor de los tres.

from os import system

menor = None
i = 0

while(i < 3):    
    # Condicional en caso de no haber ningun numero menor
    if(menor == None):
        numero = input("Ingrese un numero: ")
        # Se intenta castear el dato de entrada
        try:
            menor = int(numero)
            system("cls")
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", numero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            menor = None
    # Condicional si ya existe un numero menor
    else:
        numero = input("Ingrese otro numero: ")
        # Se intenta castear el dato de entrada
        try:
            numero = int(numero)
            system("cls")

            menor = numero if (numero < menor) else menor
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", numero, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            numero = None
    i += 1

system("cls")
print(f"El menor de los numeros ingresados es: {menor}")

input("Fin")