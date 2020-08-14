class Escritor():

	def __init__(self, caracter="*", espaciado=1):
		self.caracter = caracter
		self.espaciado = espaciado
		self.numero_opcion = 1

	def set_espaciado(self, espaciado):
		self.espaciado = espaciado

	def set_caracter(self, caracter):
		self.caracter = caracter

	def espaciar(self):
		for i in range(0, self.espaciado):
			print(end=" ")

	def crear_espaciado(self, tamano):
		print(self.caracter, end="")
		for i in range(0,tamano):
			print(" ", end="")
		print(self.caracter, end="\n")
		self.espaciar()

	def crear_barra(self, tamano, titulo=""):
		
		if titulo == "":
			tamano += 2
		for i in range(0,tamano):

			#Impresion del titulo a la mitad de la barra
			if i == tamano/2 and titulo != "":
				print("-{}-".format(titulo), end="")

			print(self.caracter, end="")
		print(end="\n")
		self.espaciar()

	def crear_opcion(self, tamano, opcion, enumeracion):
		tamano_opcion = int(tamano/2-len(opcion)/2)
		if enumeracion:
			aux = "{}).".format(self.numero_opcion)
			tamano_opcion -= len(aux)
			opcion = aux + opcion
			self.numero_opcion += 1
		print(self.caracter, end=" ")
		for j in range(0, tamano-len(opcion)-1):
			if j == tamano_opcion:
				print(opcion, end="")
			print(end=" ")
		print(self.caracter, end="\n")
		self.espaciar()

	def crear_menu(self, titulo, opciones, enumeracion, tamano=50):
		print()
		#BARRA SUPERIOR
		self.espaciar()
		self.crear_barra(tamano, titulo)
		tamano += len(titulo)
		
		#CREACION DEL CUERPO
		for i in range(0, len(opciones)):
			self.crear_espaciado(tamano)
			if i >= enumeracion[0] and i <= enumeracion[1]:

				self.crear_opcion(tamano, opciones[i], True)

		self.crear_espaciado(tamano)
		self.crear_barra(tamano)
		self.numero_opcion = 1
