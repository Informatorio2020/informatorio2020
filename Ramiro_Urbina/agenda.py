'''
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.

Añadir contacto

Lista de contactos

Buscar contacto

Editar contacto

Cerrar agenda
'''
class Contacto():

	def __init__(self, nombre, telefono, email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

	def contacto_existente(self, Contacto):

		if (Contacto.nombre == self.nombre):
			return True
		else:
			return False
		

class Agenda():

	def __init__(self, Contacto)