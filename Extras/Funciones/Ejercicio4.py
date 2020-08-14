#Ejercicio 4:
# Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. 
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

def intermedio(a, b):
    return round(((a + b) / 2), 2)

print(f"El punto intermedio entre -12 y 24 es: {intermedio(-12, 24)}")

input("\nFin")