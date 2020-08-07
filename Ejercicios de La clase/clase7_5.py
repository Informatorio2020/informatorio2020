def funcion():
	"""
	Funcion que pide que se ingrese un nombre
	return: String		nombre de la persona
	"""
	variable= input("Ingrese un nombre")
	print("Estoy en la funcion")
	return variable

variable = funcion()
funcion()
print(variable)