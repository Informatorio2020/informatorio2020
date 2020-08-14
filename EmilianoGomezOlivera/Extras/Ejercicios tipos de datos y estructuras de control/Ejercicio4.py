#Ejercicio 4:
# Escribí un programa que solicite al usuario el ingreso de una 
# temperatura en escala Fahrenheit (debe permitir decimales) y 
# le muestre el equivalente en grados Celsius. La fórmula de 
# conversión que se usa para este cálculo es: 
# °Celsius = (5/9) *(°Fahrenheit-32).

from os import system

temperaturaF = None

# Bucle que se repite hasta que se ingrese un numero valido
while(True):
    # Se solicita la temperatura
    if(temperaturaF == None):
        temperaturaF = input("Ingrese una temperatura en Fahrenheit: ")
        # Se intenta castear el dato de entrada
        try:
            temperaturaF = float(temperaturaF)
            system("cls")
        # Si no se puede convertir debido a que no es un numero caeria en esta excepcion
        except ValueError:
            print("'", temperaturaF, "' no se puede convertir a numero")
            # Se asigna la variable en None debido al error de conversion
            temperaturaF = None

    # Si se tienen todos los numeros se finaliza el bucle
    else:
        break

# Finalmentes se realiza la converison de temperaturas
print(temperaturaF, "ºF es igual a ", round(((5 / 9) * (temperaturaF - 32)), 1), "ºC")
input("\nFin")