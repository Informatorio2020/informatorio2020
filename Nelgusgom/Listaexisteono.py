#Desarrollar una función que recibe una lista y el elemento a buscar,
#devolviendo su posición si existe y -1 en caso de que no.

lista = [1,2,"Hola",5.6]

def buscar_lista(lista, valor):
	i = 0
	try:
		while True:
			if lista[i] == valor:
				indice = i
				break
			i += 1
	except IndexError:
		indice = -1
	finally:
		return indice

def buscar_lista_2(lista, valor):
	try:
		indice = lista.index(valor)
	except ValueError:
		indice = -1
	finally:
		return indice

print(buscar_lista(lista,1))
print(buscar_lista(lista,10))

print(buscar_lista_2(lista,2))
print(buscar_lista_2(lista,10))
