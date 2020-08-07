#Diseñar una función que recibe una lista y un índice, y devuelve el elemento que ocupa dicha 
#posición o None si el indice esta fuera de los limites de la lista.


def funcion(lista, indice):
	try:
		elemento = lista[indice]
	except IndexError:
		elemento = None
	return elemento



lista = [2,3,4,5,6]

print(funcion(lista, 7)) #None
print(funcion(lista, 4)) #6
print(funcion(lista, "hola")) #Error