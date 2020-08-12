#Escribir un programa que pregunte por una muestra de números, separados por comas, 
#los guarde en una lista y muestre por pantalla su media y desviación típica.
#numero ="1, 5356, 4, 5"


lista = []
numeros = input("Lista de numeros separados por comas")
valido="1234567890"
auxiliar = ""

for i in numeros:
	if i in valido:
		auxiliar = auxiliar + i
	else: 
		if auxiliar != "":
			lista.append(auxiliar)
			auxiliar = ""


if auxiliar != "":
	lista.append(auxiliar)

print(lista)
