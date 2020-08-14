#Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80,
# 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]

print("Dado la siguiente lista de precios: ")
print(precios)
precios.sort()
print(f"\nEl menor es {precios[0]} y el mayor es {precios[-1]}")


input("\nFin")