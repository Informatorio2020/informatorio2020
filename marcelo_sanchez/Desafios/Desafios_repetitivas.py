# DESAFIO 1 - SISTEMA LOGIN
"""
bandera = 0

while bandera < 4:
	contraseña = input("Ingrese la contraseña:\n\t")
	if contraseña == "AB1":
		print("Ha ingresado correctamente al sistema.")
		bandera = 4
	else:
		bandera += 1
		print("Contraseña incorrecta.\n\n")

if bandera > 4 or contraseña != "AB1":
	print("Ha superado los intentos permitidos.\n\n")
"""

# DESAFIO 2
"""
bandera = True
menos_100 = 0
menos_200 = 0
mas_200 = 0
total_personas = 0

while bandera:
	colillas = float(input("Ingrese la cantidad de colillas que recolectó:\n\t"))
	if colillas < 100:
		menos_100 += 1
		total_personas += 1
	elif colillas > 100 and colillas < 200:
		menos_200 += 1
		total_personas += 1
	elif colillas > 200:
		mas_200 += 1
		total_personas += 1
	else:
		printf("Ingreso un numero negativo o incorrecto. Intente de nuevo.")
		continue
	respuesta = int(input("CONTINUAR O SALIR? 01-CONITNUAR 02-SALIR\t"))
	if respuesta == 2:
		bandera = False

print("\n\nCantidad de colillas\t\tPorcentaje de personas\n")
print("Menos de 100 colillas\t\t", "{:.2f}".format(menos_100*100/total_personas), "%")
print("Mas de 100 y menos de 200\t", "{:.2f}".format(menos_200*100/total_personas), "%")
print("Mas de 200\t\t\t", "{:.2f}".format(mas_200*100/total_personas), "%\n\n")
"""

#DESAFIO 3
"""
bandera = True

while bandera:
	importe = float(input("Ingrese importe a pagar:\n\t"))
	cod_descuento = int(input("Ingrese cod de descuento: 1-ROJO 2-AMARILLO 3-BLANCA\n\t"))

	if cod_descuento == 1:
		importe_total = importe * 0.60
		print("\nIMPORTE TOTAL: $", "{:.2f}".format(importe_total))
	elif cod_descuento == 2:
		importe_total = importe * 0.75
		print("\nIMPORTE TOTAL: $", "{:.2f}".format(importe_total))
	elif cod_descuento == 3:
		print("\nIMPORTE TOTAL: $", importe)
	else:
		print("\nIngreso un dato incorrecto. Intente de nuevo.")
		continue
	respuesta = int(input("\nContinuar ingresando datos? 01-SI 02-NO\n"))
	if respuesta == 2:
		bandera = False

print("\n\nHa salido con éxito del programa.")
"""

#DESAFIO 4

"""
filas = int(input("Ingrese la cantidad de filas:\n\t"))
columnas = int(input("Ingrese la cantidad de columnas:\n\t"))
bandera = "blanco"

for i in range(0, filas):
	for j in range(0, columnas):
		if bandera == "blanco":
			print("VERDE", end = " ")
			bandera = "verde"
		else:
			print("BLANCO", end = " ")
			bandera = "blanco"

	print("\n")
"""
	
#DESAFIO 5
"""
cantidad_vehiculos = 0
tiraron_basura = 0
multados = 0
lista_vehiculos = []
bandera = True

while bandera:
	patente = input("Ingrese la patente conformada por 3 números y 3 letras:\n\t")
	respuesta_basura = int(input("Arrojó basura? 01-SI 00-NO:\n\t"))
	respuesta_multa = int(input("Ya tenía multas? 01-SI 00-NO:\n\t"))
	if respuesta_basura == 1:
		tiraron_basura += 1
	if respuesta_multa == 1:
		multados += 1

	patente = patente + str(respuesta_basura) + str(respuesta_multa)
	lista_vehiculos.append(patente)

	respuesta_while = int(input("Continuar ingresando datos? 01-SI 00-NO:\n\t"))
	if respuesta_while == 0:
		bandera = False

print("Patentes registradas: ", lista_vehiculos)
print("Cantidad de vehículos observados: ", len(lista_vehiculos))
print("Cantidad de vehículos que arrojaron basura: ", tiraron_basura)
print("\tVehículos que tiraron basura y tenían al menos una multa: ", float("{:.2f}".format(multados*100/tiraron_basura)), "%")
"""