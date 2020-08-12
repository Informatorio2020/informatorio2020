#Ejercicio 8:
#Crear una función que reciba una lista y calcule la suma de todos los elementos
#devolviendo None en caso de que alguno de ellos no pueda sumarse.

lista=[1, 3, 4, 5, 7]

def sumalis(lista):
	acu = 0
	try:
		for x in lista:
			acu = acu + x

	except TypeError:
		print("Error no se pueden sumar cadenas con números")
		acu= None
		
	finally:
		return acu

print(sumalis(lista))