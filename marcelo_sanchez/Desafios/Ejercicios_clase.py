# EJERCICIO 2
""""
lista = []

for i in range(0, 3):
	asignatura = input("Ingrese el nombre de la asignatura: ")
	lista.append(asignatura)

for elemento in lista:
	print("Yo estudio ", elemento)
"""
"""
lista = []

for i in range(0, 3):
	asignatura = input("Ingrese el nombre de la asignatura:\t")
	nota = int(input("Ingrese su nota:\t"))
	asignatura_nota.append(asignatura, nota)
	lista.append()

	for i in range(len(lista)):
		print("En ", lista[i][i][i+1])
"""

# FUNCIONES
"""
def tiempo_degradacion(elemento = "No existe\n"):
	if elemento == "bolsa de plastico" or "bolsa de plástico":
		return "Tarda 150 años en desaparecer\n\n"
	elif elemento == "botella de pet":
		return "Tarda 1000 años en desaparecer\n\n"
	elif elemento == "chicle":
		return "Tarda 5 años en desaparecer\n\n"
	elif elemento == "envase tetrabik":
		return "Tarda 30 años en desaparecer\n\n"
	else:
		return "Elemento inexistente. Intente de nuevo.\n\n"
		tiempo_degradacion(elemento)

elemento = input
"""
"""
def area_circulo(radio):
	return radio**2*3.14159

print(area_circulo(5))
"""
#Ejercicio 4
"""
def intermedio(a, b):
	return (a + b)/2

print(intermedio(-12, 24))
"""

# Ejercicio 5
""" INCOMPLETO
lista = [1, 4, 5, 6, 11, 23, 24]
lista2 = []

def separar(lista):
	lista2 = [i for i in lista if i%2 != 0]
	lista2.sort()
	lista = [i for i in lista if i%2 == 0]
	lista.sort()

separar(lista)
print("Lista ordenada con números impares: ", lista2)
print("Lista ordenada con números paresL ", lista)
"""
"""
def mensaje():
	return "Hola Mundo"
def llamada_de_retorno(funcion="" ):
	return globals()[funcion]()

print(llamada_de_retorno("mensaje"))
nombre_de_la_funcion = "mensaje"
print(locals()[nombre_de_la_funcion])
"""
def invocadora(funcion):
	if funcion in globals():
		return globals()[funcion]() + "\ny esta la funcion invocadora\n\n"
	else:
		return "Dicha funcion no se encontró en el diccionario de variables globales. F.\n\n"

def cadena():
	return "Este return pertenece a la funcion cadena"

print(invocadora("cadena1"))

