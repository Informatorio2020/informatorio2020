"""Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo 
en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número 
entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado 
de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla 
el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de 
la operación."""


decimales = float(input("ingresar un número con decimales"))
entero = int(input("ingrese un número entero"))

suma = decimales + entero

print("El resultado de la suma es: ", suma ," donde el numero con decimales es: ", str(decimales), entero)