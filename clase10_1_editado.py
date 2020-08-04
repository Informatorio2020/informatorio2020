#Un número primo es un número entero mayor que 1 que solo es divisible por uno y por sí mismo. 
#Escriba una función que determine si su parámetro es primo o no, devolviendo True si lo es y 
#False en caso contrario. Escriba un programa principal que lea un número entero del usuario y 
#muestre un mensaje que indique si es primo o no. Asegúrese de que el programa principal no 
#se ejecutará si el archivo que contiene su solución se importa a otro programa.


def funcion(numero):
	bandera = True
	for i in range(2, numero):
		print(i)
		if (numero % i) == 0:
			bandera= False
	return bandera



numero = int(input("Ingrese un numero"))

