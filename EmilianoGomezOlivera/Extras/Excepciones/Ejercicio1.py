# Ejercicio 1:
# Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
# segundo, capturar la excepción ZeroDivisionError.

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return f"{ZeroDivisionError.__name__}: No se puede dividir por cero."
    except TypeError:
        return f"{TypeError.__name__}: Uno de los valores ingresados es invalido, solo pueden ser numeros."


print(division(1, 1))
print(division(1, 0))
print(division(1, "HOLA"))

input("\nFin")