"""
Esto tengo hasta ahora 
no se si estará bien o no
pero es lo que me va saliendo
"""

class Contacto:
	def __init__(self,nombre,telefono,email):	
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

#Método agregar: agrega contactos
	def agregar(self):
		agenda[self.nombre] = [self.telefono, self.email]

#Método lista: muestra lista de contactos	
	def lista(self):
		lista_Contactos.append(self.nombre)
#Buscar contacto: busca contacto por nombre
	def getnombre(self):
		return self.nombre
#Editar contacto: Edita contacto
	def setnombre(self,a):
		self.nombre = a

	def setemail(self,b):
		self.email = b
		
	def settelefono(self,c):
		self.telefono = c

	



lista_Contactos = []
agenda = {}

nombre = input('Nombre: ')
telefono = input('Telefono: ')
email = input('Email: ')

registro = Contacto(nombre,telefono, email)
registro.agregar()
registro.lista()

print(registro)

