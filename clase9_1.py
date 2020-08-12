
#Escribir un programa que pregunte por una muestra de números, separados por comas, 
#los guarde en una lista y muestre por pantalla su media y desviación típica.
#numero ="1, 53, 4, 5"

lista =[]
numeros = input("Ingrese los numeros separados por una coma")
longitud = len(numeros)
indice = 0
auxiliar=""

while longitud > indice:
	if numeros[indice] != "," and numeros[indice] != " " :
		auxiliar = auxiliar + numeros[indice]
	else:
		if auxiliar != "":
			lista.append(auxiliar)
		auxiliar = ""

	indice = indice + 1 

if auxiliar != "":
	lista.append(auxiliar)

print(lista)