class Persona:
	def __init__(self, nombre, dni):
		self.nombre = nombre
		self.dni = dni
		self.data = {}
	def __str__(self):
		return "es de clase Persona {}".formar(self.dni)

class Paciente(Persona, Otra_clase):
	def __init__(self,nombre, dni, historia_clinica):
		Persona.__init__(self,nombre,dni)
		self.historia_clinica = historia_clinica
	def __str__(self):
		return "es de clase Paciente {}, dni nro {}".format(self.nombre,self.dni)

Persona1 = Persona( "nelson", 203338643)
Persona2 = Persona( "Gabriel", 39225552)
Paciente1 = Paciente("Lilian", 22665765, "HC N! 1234")
Paciente1 = Paciente("Martin", 42190411, "HC N! 5678")

print(Paciente1.nombre)
print(Paciente1)
print(Persona1)





class Contacto():
	agenda = []
	def __init__(self, nombre, telefono, email):
		self.nombre= nombre
		self.telefono = telefono
		self.email = email

	def __str__(self):
		return "Nombre: {} - Teléfono: {} - Email: {}".format(self.nombre,self.telefono,self.email)

	def aniadir(self):
		Contacto.agenda.append(self)#[self.nombre] = [self.telefono,self.email]


	def listar(self):
		for a in Contacto.agenda:
			print(a)

	def buscar(self, nombre):
		for a in Contacto.agenda:
			if a.nombre == nombre:
				print(a)

	def editar(self, editar):
		for a in Contacto.agenda:
			if a.nombre == editar:            
				a.nombre = input("Ingrese el nombre:")
				a.telefono = input("Ingrese el teléfono:")
				a.email = input("Ingrese el email:")
				return("Contacto editado")
				return("No se encuentra el contacto")