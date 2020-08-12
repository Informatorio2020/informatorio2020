lista = []
i = 1

while i == 1:
	cantidad = int(input("Cuanto conoce usted sobre contaminación?, valore del 1 al 10: "))
	i = 0

i = 1

#while (opcion == 1) and (cantidad >= 1) and (cantidad <= 10):
	#cantidad = int(input("Cuanto conoce usted sobre contaminación?, valore del 1 al 10:"))
	#lista.append(cantidad)
	#break

while cantidad >= 1 and i == 1: 
	lista.append(cantidad)

	if cantidad <= 10:
		pregunta = int(input("Ingrese 1 si quiere continuar o 0 para finalizar: "))
		if pregunta == 1:
			cantidad = int(input("Cuanto conoce usted sobre contaminación?, valore del 1 al 10: "))
		elif pregunta == 0:
			i = 0
			for recorrido in range(1,len(lista)):
				for posicion in range(len(lista) - recorrido):
					if lista[posicion] < lista[posicion + 1]:
						temp = lista[posicion]
						lista[posicion] = lista[posicion + 1]
						lista[posicion + 1] = temp
			print("Su lista es: ", lista)
		else:
			i = 1

	else:
		cantidad = int(input("Numero incorrecto, por favor elija nuevamente del 1 al 10: "))