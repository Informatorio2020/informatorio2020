#Crear una funcion que cargue una lista con datos ingresados por el usuario
#Crear una fucion que elimine los elementos repetidos
#Crear una funcion que muestre el contenido de la lista de forma estetica


def cargar_lista(lista, elemento):
	lista.append(elemento)


def elimina_repetidos(lista):
	auxiliar= []
	for elemento in lista:
		if elemento not in auxiliar:
			auxiliar.append(elemento)

	return auxiliar

def eliminar_repetidos_2(lista):
	for i in range(len(lista)-1):
		for j in range(i+1, len(lista)):
			print(" {} {}".format(i,j))
			try:
				if lista[i]==lista[j]:
					del lista[j]
			except:
				pass

	print(lista)


lista2 = [1,2,3,4,5,1,2,3,6,7,8,4,5]


lista = []

elemento= input("Ingrese el elemento a agregar. Para salir ingrese 0")

while elemento != "0":
	cargar_lista(lista, elemento)
	elemento= input("Ingrese el elemento a agregar. Para salir ingrese 0")


print(lista)

print(elimina_repetidos(lista))

print("segunda funcion")
eliminar_repetidos_2(lista2)


