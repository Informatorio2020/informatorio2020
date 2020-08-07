# Ejercicio 8
"""
def sumar_lista(lista):
	try:
		suma = sum(lista)
	except TypeError:
		suma = None
	finally:
		return suma

lista = [1, 2, 3]
print(sumar_lista(lista))
"""

# Ejercicio 9
"""" 
def encontrar_item(lista, indice):
	try:
		elemento = lista[indice]
	except IndexError:
		elemento = None
	
	return elemento

lista = [1, 2, 3, "hola"]
print(encontrar_item(lista, 2))
"""

# Ejercicio 7

def encontrar_elemento(lista, elemento):
	posicion = 0
	try:
		posicion = lista.index(elemento)
	except:
		posicion = -1

	return posicion

lista = [1, 2, 3, "holA", "44"]

elemento = int(input("Elemento a buscar: "))
print("Posicion del elemento: ", encontrar_elemento(lista, elemento))
