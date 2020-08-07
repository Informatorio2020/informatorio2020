# PARA PROBAR LOS PROGRAMAS ELIMINAR LAS """ al inicio y al final de cada bloque de codigo.

# DESAFIO 1
""""
iteracion = True

while iteracion:
	años = int(input("Ingrese la cantidad de años que utilizo el insecticida: "))
	print()
	if años >= 10:
		print("Por favor solicite revisión de suelos en su plantación/n")
	else:
		print("Intentaremos ayudarte con un nuevo sistema de control de plagas y cuidaremos tu suelo/n")

	respuesta = input("Desea continuar ingresando datos?: 1-SI 0-NO: ")
	respuesta = int(respuesta)
	print()
	if respuesta == 0:
		iteracion = False

print("Ha salido con exito del programa.")
"""

# DESAFIO 2
"""
bandera = True

while bandera:
	pez_tamaño = int(input("Ingrese el tamaño del pez 1-NORMAL 2-DEBAJO DE NORMAL 3- ENCIMA DE NORMAL 4- SOBREDIMENSIONADO:\n\t"))
	if pez_tamaño == 1:
		print("\tPez en buenas condiciones")
	elif pez_tamaño == 2:
		print("\tPez con problemas de nutrición")
	elif pez_tamaño == 3:
		print("\tPez con síntomas de organismo contaminado")
	elif pez_tamaño == 4:
		print("\tPez contaminado")
	else:
		print("\tOpcion incorrecta. Intente de nuevo.")

	respuesta = int(input("Desea continuar o salir del programa? 1-CONTINUAR 2-SALIR:\n\t"))
	if respuesta == 2:
		bandera = False
	print()

print("Ha salido del programa con éxito.")

"""

# DESAFIO 3
"""
bandera = True

while bandera:
	compuesto = float(input("Ingrese en porcentajes '%' cuanto abarca su compuesto en el suelo:\n\t"))
	matorral = int(input("Hay presencia de matorral? Ingrese: 1-SI 2-NO\n\t"))
	if matorral == 2 and compuesto >= 10:
		print("Es factible utilizar fertilizantes en sus suelos.")
	else:
		print("No es factible utilizar fertilizantes en sus suelos.")
	respuesta = int(input("Desea continuar o salir del programa? Ingrese: 1-CONTINUAR 2-SALIR\n\t"))
	print()
	print()
	if respuesta == 2:
		bandera = False
print("Ha salido del programa con éxito.")
"""

# DESAFIO 4
"""
bandera = True

while bandera:
	receta = int(input("Elija una receta ingresando 1 o 2 para cada opcion respectivamente:\n\t"))
	if receta == 1:
		print("Ingredientes disponibles para elegir (solo 3):\n\tComunes: Verduras y Berenjena.\n\tDe receta: Lentejas y Apio.")
		ingredientes_elegidos = input("Ingrese los ingredientes separados por coma:\n\t")
		print("Receta elegida: 1.\n\tIngredientes: ", ingredientes_elegidos)
	elif receta == 2:
		print("Ingredientes disponibles para elegir (solo 3):\n\tComunes: Verduras y Berenjena.\n\tDe receta: Morrón y Cebolla.")
		ingredientes_elegidos = input("Ingrese los ingredientes separados por coma:\n\t")
		print("Receta elegida: 2.\n\tIngredientes: ", ingredientes_elegidos)
	else:
		print("Opcion incorrecta. Intente de nuevo.")
		continue
		
	respuesta = int(input("\nDesea continuar o salir del programa? 1-CONTINUAR 2-SALIR\n\t"))
	if respuesta == 2:
		bandera = False

print("\nHa salido del programa con éxito.\n\n")
"""

# DESAFIO 5
"""
bandera = True

while bandera:
	barrio = input("\nIngrese el nombre del barrio:\n\t")
	barrio = barrio.lower()
	ubicacion = int(input("Ingrese ubicacion del barrio: 1-CENTRICO 2-NO CENTRICO\n\t"))

	if barrio < 'm' and ubicacion == 1:
		print("Se encuentra en la SECCION A")
	elif barrio > 'm' and ubicacion == 2:
		print("Se encuentra en la SECCION A")
	elif barrio >= 'm' and ubicacion == 1:
		print("Se encuentra en la SECCION B.")
	elif barrio <= 'm' and ubicacion == 2:
		print("Se encuentra en la SECCION B.")
	else:
		print("Ingresó una opción incorrecta. Intente de nuevo.\n\n")
		continue

	respuesta = int(input("\nDesea continuar ingresando datos? Ingrese segun corresponda: 1-SI 2-NO\n\t"))
	if respuesta == 2:
		bandera = False

print("\n\nHa salido del programa con éxito.")
"""