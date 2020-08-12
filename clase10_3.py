#DEFINIR UNA FUNCION
#Funcion sin parametros
def nombre_de_la_funcion():
	print("Instrucciones de la funcion")
	#Retornar algo
	return "Hola"

#Funcion con parametro
def funcion_2(parametro1, parametro2):
	#retorna concatenacion de los parametros
	return parametro1 + parametro2

#Funcion con parametro con valores por defecto
def funcion_3(parametro1="Hola", parametro2= ""):
	#retorna concatenacion de los parametros
	return parametro1 + parametro2

variable = nombre_de_la_funcion()

print(variable)

variable_2= funcion_2("Hola ", "mundo")

print(variable_2)

variable_3 = funcion_2(parametro2= "estas?", parametro1= "¿como")
print(variable_3)

variable_4= funcion_3("Hola", " mundo")
print(variable_4)

variable_4 = funcion_3()
print(variable_4)

variable_4 = funcion_3(parametro2= "¿como estas?")
print(variable_4)