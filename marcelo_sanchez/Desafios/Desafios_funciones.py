# DESAFIO 1

"""
def tiempo_degradacion(elemento = "No existe\n"): # Funcion con condicionales múltiples
	if elemento == 1:
		return "\nTarda 150 años en desaparecer\n\n"
	elif elemento == 2:
		return "\nTarda 1000 años en desaparecer\n\n"
	elif elemento == 3:
		return "\nTarda 5 años en desaparecer\n\n"
	elif elemento == 4:
		return "\nTarda 30 años en desaparecer\n\n"
	else:
		return "\nElemento inexistente. Intente de nuevo.\n\n"

respuesta_control = -1 # Variable de control inicializada en -1 para que se ejecute al menos 1 vez

while respuesta_control != 0:
	print("\nElija un elemento para saber su tiempo de degradación:\n")
	elemento = int(input("\t01- Bolsa de plastico\n\t02- Botella de pet\n\t03- Chicle\n\t04- Envase tetrabik\n\n"))
	print(tiempo_degradacion(elemento)) # Se imprime lo que retorna la función
	respuesta_control = int(input("¿Continuar? 01-SI 00-NO\n"))
"""

# DESAFIO 2

"""
ciudades_toneladas = {}
def relacion(clave_a, clave_b, diccionario):
	if diccionario[clave_a] > diccionario[clave_b]:
		return "Ciudad con más toneladas: " + clave_a
	elif diccionario[clave_a] < diccionario[clave_b]:
		return "Ciudad con más toneladas: " + clave_b
	else:
		return "Ciudades con igual cantidad de reciclado: " + clave_a + " y " + clave_b

respuesta_control = -1

while respuesta_control != 0:
	print("Ingrese el nombre de la ciudad y luego las toneladas de basura reciclada\n")
	ciudad_a = input("Nombre: ")
	toneladas = int(input("Cantidad de toneladas: "))
	ciudades_toneladas.setdefault(ciudad_a, toneladas) # se agrega el par ciudad(key): toneladas (valor) al diccionario
	print("\nIngrese el nombre de la segunda ciudad y luego las toneladas de basura reciclada\n")
	ciudad_b = input("Nombre: ")
	toneladas = int(input("Cantidad de toneladas: "))

	ciudades_toneladas.setdefault(ciudad_b, toneladas) # se vuelve a agregar los datos de la ciudad 2 al diccionario
	print("\n", relacion(ciudad_a, ciudad_b, ciudades_toneladas)) # Se imprime lo que retorna la función
	respuesta_control = int(input("\n\n¿Continuar? Ingrese 01-SI o 00-NO\n\t")) # pregunta para continuar o salir del programa
"""

# DESAFIO 3

"""
arboles_ciudades = {}
lista_mayores100 = []
lista_menores_igual100 = []
ciudades_mas100 = 0
respuesta_control = -1
print("\t\tArboles por ciudad plantados durante la cuarentena.\n\n")

while respuesta_control != 0:
	ciudad = input("Nombre de la ciudad: ")
	cantidad_arboles = int(input("Arboles plantados: "))
	arboles_ciudades.setdefault(ciudad, cantidad_arboles)
	respuesta_control = int(input("\n\n¿Continuar? Ingrese 01-SI o 00-NO\n\t"))	

arboles_ciudades = list(arboles_ciudades.items()) # arboles_ciudades pasa a contener una lista, donde cada elemento de la misma
                                                  # es una tupla, que contiene ciudad (key) y cantidad de arboles plantados (valor)
print("\n\n")
print("Lista de ciudades y cantidad de arboles plantados respectivamente: \n\t", arboles_ciudades)

for i, elemento in enumerate(arboles_ciudades):
	if arboles_ciudades[i][1] > 100: # Si el valor de la key [i] es superior a 100
		lista_mayores100.append(arboles_ciudades[i]) # Agrego en forma de una tupla (key:valor) a la lista mayores de 100.
		ciudades_mas100 += 1
	else:
		lista_menores_igual100.append(arboles_ciudades[i]) # Sino es superior a 100, se agrega la tupla (key:valor) a la lista menores o iguales que 100.
print("Ciudades con más de 100 árboles plantados:\n\t", lista_mayores100)
print("Ciudades con menos de 100 árboles plantados:\n\t", lista_menores_igual100)

# A través del argumento key = le digo al metodo sort() que use como parametro de ordenación la posicion 1 de cada tupla de mi lista (es decir, usa el valor no la key que está en la posicion 0).
lista_mayores100.sort(key = lambda item_tupla : item_tupla[1]) 
lista_menores_igual100.sort(key = lambda item_tupla : item_tupla[1])

print("\n\nLista ORDENADA con cantidades de arboles superiores a 100:\n\t", lista_mayores100)
print("\nLista ORDENADA con cantidades de arboles menores o iguales a 100:\n\t", lista_menores_igual100)
print("\nCantidad de ciudades que plantaron más de 100 arboles:\n\t", ciudades_mas100)
"""