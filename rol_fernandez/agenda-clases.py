class Contacto():

	def __init__ (self, nombre, telefono, email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

agenda ={}

usuario_nombre = input("Nombre: ")
usuario_telefono = input("Telefono: ")
usuario_email = input("e-mail: ")

registro=Contacto(usuario_nombre, usuario_telefono, usuario_email)

print("Nombre:",usuario_nombre, "Telefono:",usuario_telefono, "E-Mail:",usuario_email)