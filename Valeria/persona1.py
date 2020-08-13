class Persona():
	def __init__(self, nombre, dni):
		self.nombre = nombre
		self.dni = dni


class Paciente(Persona):
	def __init__(self, historia_clinica, nombre, dni):
		self.historia_clinica = historia_clinica
		super().__init__(nombre, dni)

	def __str__(self):
		return self.nombre

	def __str__(self):
		return "Este paciente se llama {}".format(self.nombre)

paciente = Paciente(2356, nombre= "Valeria", dni=36115830)
print(paciente.nombre)
print(paciente)
