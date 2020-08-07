class Persona:
	def __init__(self, nombre, dni):
		self.nombre = nombre
		self.dni = dni


class Paciente(Persona):
	def __init__(self, nombre, dni, historia_clinica):
		Persona.__init__(self, nombre, dni)
		self.historia_clinica = historia_clinica

Persona1 = Persona("Nelson", 20338643)
Persona2 = Persona("Gabriel", 39225552)
Paciente1 = Paciente("Lilian", 22665765,"HC N° 1234")
Paciente2 = Paciente("Martin", 42190411,"HC N° 5678")
print(Persona1.nombre)
print(Paciente1.nombre)