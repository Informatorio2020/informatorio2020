class triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

class tipo_de_triangulo(triangulo):
	def __init__(self, lado1, lado2, lado3):
		triangulo.__init__(self, lado1, lado2, lado3)

	def segun_lados(self):
		lista_auxiliar = [self.lado1, self.lado2, self.lado3]
		lista_auxiliar.sort()
		print (lista_auxiliar[2])
		if self.lado1 == self.lado2 == self.lado3:
			print("Es un triángulo equilátero.")
		elif self.lado1 == self.lado2 != self.lado3 or self.lado2 == self.lado3 != self.lado1 or self.lado1 == self.lado3 != self.lado2:
			print("Es un triángulo isósceles.")
		else:
			print("Es un triángulo escaleno.")

triangulo1 = tipo_de_triangulo(5, 7, 6)
print(triangulo1.segun_lados())