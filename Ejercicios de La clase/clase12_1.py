#Diccionarios
a = {}

a = {"clave": "valor"}

a = dict()

#Funciones
# Mostrar los numeros del 1 al 10
def funcion():
	for i in range(1, 11):
		print(i)


#Funcion que retorna varios valores ademas de la sumad de dos numeros
def funcion_2(a, b):
	return a+b, "Hola", 234
	print("hola")

#Funcion que retorna las claves de un diccionario o un mensaje
def funcion_3(diccionario = None):
	if not diccionario:
		retorno = "El diccionario esta vacio"
	else:
		retorno = diccionario.keys()
	return retorno

variable= funcion_2(12, 5)
print(variable)

variable_2= funcion_3({"hola":2, "como":3, "estas":4})
print(variable_2)

variable_3 = funcion_3()

print(variable_3)