#Ejercicio 3:
# Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
# segundo, capturar las excepciones ZeroDivisionError y ValueError.

def division():
    try:
        x = int(input("Ingrese el primer numero: "))
        y = int(input("Ingrese el segundo numero: "))
        return x / y
    except ZeroDivisionError:
        return f"{ZeroDivisionError.__name__}: No se puede dividir por cero."
    except ValueError:
        return f"{ValueError.__name__}: Uno de los valores ingresados es invalido, no puede ser convertido a numero."

print(division())
print(division())
print(division())

input("\nFin")