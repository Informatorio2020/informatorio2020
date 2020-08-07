#Escribir un programa que pregunte por una muestra de números, separados por comas, 
#los guarde en una lista y muestre por pantalla su media y desviación típica.
#numero ="1,5356,4,5 y,gt 1234"
#["1", "5356", "4", "5y", "gt1234"]


#TODO


numeros = input("Ingrese un conjunto de caracteres separados por comas")
numeros = numeros.replace(" ", "")
valido = "1234565777890,"

lista_auxiliar = []

for i in numeros:
	if i in valido:
		lista_auxiliar.append(i)


lista = numeros.split(",")

print(lista)
print(lista_auxiliar)
