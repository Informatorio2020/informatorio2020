#Ejercicio 7:
# Escribí un programa que le solicite al usuario su edad y 
# la guarde en una variable. Que luego solicite la cantidad 
# de artículos comprados en una tienda y la guarde en otra 
# variable. Finalmente, mostrar en pantalla un mensaje que 
# indique si el usuario es mayor de 18 años de edad y además 
# compró más de 1 artículo.

from os import system 

edad = None
articulos = None

while(True):
    # Se solicita al usuario su edad
    if(edad == None):
        edad = input("Ingrese su edad: ")

        # Bloque donde se prueba convertir el dato de entrada a un tipo numerico
        try:
            edad = int(edad)
            # Se verifica que la edad sea valida
            if(edad < 0):
                print("La edad no puede ser negativa")
            else:
                system("cls")
        except ValueError:
            print(f"No se pudo castear '{edad}': El dato ingresado no es un numero")
            edad = None
    # Se solicita al usuario el numero de articulos
    elif(articulos == None):
        articulos = input("Ingrese la cantidad de articulos comprados: ")

        # Bloque donde se prueba convertir el dato de entrada a un tipo numerico
        try:
            articulos = int(articulos)
            # Se verifica que la cantidad de articulos sea valida
            if(articulos < 0):
                print("La cantidad de articulos no puede ser negativa")
            else:
                system("cls")
        except ValueError:
            print(f"No se pudo castear '{articulos}': El dato ingresado no es un numero")
            articulos = None
    else:
        break

print("El usuario es mayor de edad" if (edad >= 18) else "El usuario no es mayor de edad", f"y compro {articulos} articulos" if (articulos > 0) else " y no compro ningun articulo")

input("Fin")