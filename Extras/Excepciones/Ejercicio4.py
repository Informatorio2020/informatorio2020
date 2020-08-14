#Ejercicio 4:
# Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
# segundo. Capturar cualquier tipo de excepción que se dispare.

def division():
    try:
        x = int(input("Ingrese el primer numero: "))
        y = int(input("Ingrese el segundo numero: "))
        return x / y
    except Exception as Error:
        return f"Se produjo un error en la operacion => {Error}."

print(division(), end="\n\n")
print(division(), end="\n\n")
print(division(), end="\n\n")

input("\nFin")