class Vehículo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas 

class Coche(Vehículo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		Vehículo.__init__(self, color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

auto1 = Coche("rojo", 4, 50, 400)
print(auto1.ruedas)
print(auto1.velocidad)
print(auto1.color)
