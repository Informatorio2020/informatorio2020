#estamos probando una nueva clase

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
Paciente1 = Paciente("Lilian", 22665765,"HC1234")
Paciente2 = Paciente("Martin", 42190411,"HC5678")
print("Nombre: ", Persona1.nombre," DNI nº: ", Persona1.dni)
print("Nombre: ", Paciente1.nombre," Historia clìnica nº: ", Paciente1.historia_clinica)