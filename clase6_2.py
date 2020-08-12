#A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
#B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
#C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
#D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
#E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)].


lista = []
acumulador=0
control = int(input("Ingrese un numero. Para salir ingrese 0"))

while control != 0:
	lista.append(control)
	control = int(input("Ingrese un numero. Para salir ingrese 0"))

numero= int(input("Que numero desea eliminar"))
if numero in lista:
	lista.remove(numero)
else:
	print("el numero no esta en la lista")

for numero in lista:
	acumulador = acumulador + numero
	print("La sumatoria: ", acumulador)

comparar= int(input("Ingrese el numero a acomparar"))

listanueva = [i for i in lista if i<comparar ]

for i in listanueva:
	print(i)

diccionario={}
for i in lista:
	diccionario[i]= lista.count(i)

print(diccionario)


print(lista)