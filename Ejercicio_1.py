""" 
	Fuente del ejercicio: https://sites.google.com/view/informatorio-poo/level-stone
	Ejercicio Nº: 2
	Alumno: KevinLeguiza
"""
"""
	*Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

	*Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.

	*Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de 
	ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" 
	únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

class Vehiculo():

	def __init__(self, color, ruedas):

		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		retorno = "\tColor: {}\n\tRuedas: {}".format(self.color, self.ruedas)
		return retorno

	def nombre_clase(self):
		return "Vehiculo"

	def get_ruedas(self):
		return self.ruedas

class Coche(Vehiculo):

	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		retorno = "\tVelocidad: {} Km/h\n\tCilindrada: {} Cc\n".format(self.velocidad, self.cilindrada)
		retorno += super().__str__()
		return retorno

	def nombre_clase(self):
		return "Coche"

class Camioneta(Coche, Vehiculo):

	def __init__(self, color, ruedas, velocidad, cilindrada, carga):
		super().__init__(color, ruedas, velocidad, cilindrada)
		self.carga = carga

	def __str__(self):
		retorno = "\tCarga: {} Kg\n".format(self.carga)
		retorno += super().__str__()
		return retorno

	def nombre_clase(self):
		return "Camioneta"

class Bicicleta(Vehiculo):

	def __init__(self, color, ruedas, tipo):
		super().__init__(color, ruedas)
		self.tipo = tipo

	def __str__(self):
		retorno = "\tTipo: {}\n".format(self.tipo)
		retorno += super().__str__()
		return retorno

	def nombre_clase(self):
		return "Bicicleta"

class Motocicleta(Bicicleta, Vehiculo):
	
	def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
		super().__init__(color, ruedas, tipo)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		retorno = "\tVelocidad {} Km/h\n\tCilindrada {} Cc\n".format(self.velocidad, self.cilindrada)
		retorno += super().__str__()
		return retorno

	def nombre_clase(self):
		return "Motocicleta"

def catalogar(lista, ruedas = -1):
	filtrar_ruedas = False
	if ruedas != -1:
		filtrar_ruedas = True
	vehiculos = 0
	ruedas_vehiculo = 0

	for i in lista:
		if not(filtrar_ruedas) or i.get_ruedas() == ruedas:
			print(" ",i.nombre_clase())
			print(i, end="\n\n")

lista = []
lista.append(Coche("Rojo", 4, 50, 10))
lista.append(Camioneta("Amarillo", 4, 20, 30, 200))
lista.append(Bicicleta("Azul", 2, "Deportiva"))
lista.append(Motocicleta("Verde", 2, "Urbana", 10, 8))
catalogar(lista)