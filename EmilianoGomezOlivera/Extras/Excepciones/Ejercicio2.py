#Ejercicio 2:
# Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de
# mes y mostrar seguidamente el nombre de dicho mes. Capturar la excepción IndexError.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def mostrarMes(indice):
    try:
        return meses[indice - 1]
    except IndexError:
        return f"{IndexError.__name__}: El numero de mes ingresado es invalido."
    except TypeError:
        return f"{TypeError.__name__}: El valor ingresado es invalido, solo puede ser un numero."

print(mostrarMes(1))
print(mostrarMes(13))
print(mostrarMes("X"))

input("\nFin")