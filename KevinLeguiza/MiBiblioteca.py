class Escritor():

	def espaciar(self, espaciado):
		for i in range(0, espaciado):
			print(end=" ")

	def crear_espaciado(self, tamano, espaciado):
		print("*", end="")
		for i in range(0,tamano):
			print(" ", end="")
		print("*", end="\n")
		self.espaciar(espaciado)

	def crear_barra(self, tamano, espaciado, titulo=""):
		
		if titulo == "":
			tamano += 2
		for i in range(0,tamano):

			#Impresion del titulo a la mitad de la barra
			if i == tamano/2 and titulo != "":
				print("-{}-".format(titulo), end="")

			print("*", end="")
		print(end="\n")
		self.espaciar(espaciado)

	def crear_opcion(self, tamano, espaciado, opcion):

		tamano_opcion = int(tamano/2-len(opcion)/2)
		print("*", end=" ")
		for j in range(0, tamano-len(opcion)-1):
			if j == tamano_opcion:
				print(opcion, end="")
			print(end=" ")
		print("*", end="\n")
		self.espaciar(espaciado)

	def crear_menu(self, titulo, opciones, mensaje_input="::", tamano=50, espaciado=1):
		print()
		#BARRA SUPERIOR
		self.espaciar(espaciado)
		self.crear_barra(tamano, espaciado, titulo)
		tamano += len(titulo)
		
		#CREACION DEL CUERPO
		for i in range(0,len(opciones)):
			self.crear_espaciado(tamano, espaciado)
			self.crear_opcion(tamano, espaciado, opciones[i])

		self.crear_espaciado(tamano, espaciado)
		self.crear_barra(tamano, espaciado)
		print(end="\n\n")
		self.espaciar(espaciado)
		print(mensaje_input, end=" ")
