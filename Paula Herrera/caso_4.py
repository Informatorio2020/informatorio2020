class Contacto():

	def __init__(self, nombre, telefono, email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

#Solucion 2
#Metodo
'''
	def aniadir(self):
		agenda[self.nombre] = [self.telefono, self.email]
'''

class Agenda():
	def __init__(self):
		self.lista_de_contactos = []

	def aniadir(self, dato):
		self.lista_de_contactos.append(dato)

agenda = Agenda()

nombre_usuario = input('Nombre: ')
telefono_usuario = input('Telefono: ')
email_usuario = input('Email: ')

registro = Contacto(nombre_usuario, telefono_usuario, email_usuario)

agenda.aniadir(registro)

print(agenda.lista_de_contactos)
#registro.aniadir()

#Solucion 1
#funcion
'''
def aniadir(datos):
	agenda[datos.usuario] = [datos.telefono, datos.email]

aniadir(registro)
'''