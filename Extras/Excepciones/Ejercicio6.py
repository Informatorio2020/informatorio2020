#Ejercicio 6:
# Desarrollar una función que reciba dos enteros y divide el mayor por el menor, mostrando
# un mensaje de error si eso significa dividir entre cero. Escribir un programa que utilice esta
# función, pidiendo los valores al usuario.

def division():
    try:
        x = int(input("Ingrese el primer numero: "))
        y = int(input("Ingrese el segundo numero: "))
        return (x / y) if (x > y) else (y / x)
    except ZeroDivisionError:
        return f"{ZeroDivisionError.__name__}: No se puede dividir por cero."
    except Exception as Error:
        return f"Se produjo un error en la operacion => {Error}."

print(division(), end="\n\n")
print(division(), end="\n\n")
print(division(), end="\n\n")

input("\nFin")