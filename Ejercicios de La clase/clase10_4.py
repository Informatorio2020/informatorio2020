#Argumentos indeterminados por posicion
# Toma los argumentos y los convierte en un tupla
def funcion_1(*variable):
	print(variable)
	for i in variable:
		print(i)


funcion_1("1", 3, "hola", 2335)

funcion_1(1)

funcion_1([1,3,4], "hola")

#Argumentos indeterminados por nombre
def funcion_2(**kwargs):
	print(kwargs)
	for i in kwargs:
		print(i, ":", kwargs[i])


funcion_2(valor_1="hola", valor_2= "mundo", valor_3=45435)

funcion_2(clave= "valor")

funcion_2(v1=2, v2=5, v3=8, v4=9)

def funcion_3(*args, **Kwargs):
	print(args)
	print(Kwargs)

funcion_3(2, "hola", "5667", valor_3="valor_3", clave1="clave", key1="otro valor")

def funcion_4(*args):
	print("Hola ")
	for i in args:
		print(i, end="") 
	print()

funcion_4("Mariana Elena", "Nuñez")

funcion_4("Mariana", "Elena", "Nuñez")

funcion_4("Juan", "Pedro", "Perez", "Gonzales")