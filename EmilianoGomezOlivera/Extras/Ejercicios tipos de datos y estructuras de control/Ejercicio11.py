#Ejercicio 11:
# Escribí un programa que muestre la sumatoria de todos los números entre el 0 y el 100. 

sumatoria = 0

# El bucle va hasta el 101 con el fin de incluir al 100
for i in range(101):
    sumatoria += i

print(f"El resultado de la sumatoria del rango [0..100] es: {sumatoria}")    

input("Fin")