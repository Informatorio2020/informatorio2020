#Clases

class Auto:
	ruedas = 4
	def __init__(self, color):
		self.id = math.random(1,10)
		self.color = color

	def __str__(self):
		return "Este es un auto de color {}".format(self.color)

	def arrancar(self):
		print("El auto de color {} arranco".format(self.color))



class Mesa:
	def __init__(self, color, tamano):
		self.color= color
		self.tamano= tamano

	def __str__(self):
		return "Esta es una mesa de color {} y de tamaño {}".format(self.color, self.tamano)



auto1 = Auto("rojo")

auto2 = Auto("Azul")

auto3 = Auto("Negro")

print(auto1.color)
print(auto2.color)
print(auto3.color)
print(auto3)

auto1.color = "dorado"

auto1.arrancar()

auto2.arrancar()

mesa = Mesa("blanca", "mediana")
print(mesa.tamano)
print(mesa)
