#DESAFIO 1
"""

bandera = True
lista = []

while bandera:
	respuesta_contaminacion = int(input("Cuánto sabes de contaminación del 1 al 10?:\n\t"))
	lista.append(respuesta_contaminacion)
	respuesta = int(input("Desea seguir ingresando datos? 01-SI 02-NO\n\t"))
	if respuesta == 2:
		bandera = False
lista.sort()
print("Resultados de la encuesta:\n\t", lista)
"""

#DESAFIO 2

"""
bandera = True
contaminacion_mar = ('aguas residuales', 'químicos tóxicos', 'aguas pluviales', 'vertido de plásticos', 'vertidos de petróleo', 'actividad minera')
longitud_tupla = len(contaminacion_mar)

while bandera:
	numero = int(input("Ingresa un número positivo cualquiera\n\t"))
	if numero <= longitud_tupla:
		print("Ese número corresponde al factor ", contaminacion_mar[numero], "de los ", longitud_tupla, " más dañinos para el mar.\n")
	else:
		print("El número no coincide con ningún factor de la lista!\n")	

	respuesta = int(input("Continuar ingresando números? 01-SI 00-NO:\n\t"))
	if respuesta == 0:
		bandera = False

print("Ha salido con éxito del programa.\n\n")
"""

#DESAFIO 3

"""
bandera = True
emails_biologos = {}

while bandera:
	nombre = input("Ingrese el nombre del biólogo o bióloga:\n\t")
	nombre = nombre.lower()
	email = input("Ingrese su email:\n\t")
	if nombre not in emails_biologos:
		emails_biologos.setdefault(nombre, email)
	else:
		print("No se pueden agregar nombres repetidos. Intente de nuevo.")
		continue

	respuesta = int(input("Continuar ingresando datos?: 01-SI 00-NO\n\t"))
	if respuesta == 0:
		bandera = False

print("Lista de biólogos con sus respectivos emails:\n\t", emails_biologos)
print("Ha salido con éxito del programa.\n\n")
""" 

#DESAFIO 4
"""
bandera = True
especies = []
especies_tupla = ()
i = 0

while bandera:
	nombre_especie = input("Ingrese el nombre de la especie:\n\t")
	especies.append(nombre_especie)
	print("\tHola soy ", especies[i], " cuidame.\n\n")
	i += 1
	respuesta = int(input("CONTINUAR? 01- SI 00-NO: "))
	if respuesta == 0:
		bandera = False

especies_tupla = tuple(especies)
print(especies)
"""