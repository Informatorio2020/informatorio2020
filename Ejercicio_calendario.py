"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones.

    Añadir contacto

    Lista de contactos

    Buscar contacto

    Editar contacto

    Cerrar agenda
"""

#Importacion de libreria para el uso de la funcion system("cls") para limpiar la pantalla
from os import system

#Clase contacto
class contacto():

	def __init__(self, nombre, telefono, email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

	def get_nombre(self):
		return self.nombre

	def get_telefono(self):
		return self.telefono

	def get_email(self):
		return self.email

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_telefono(self, telefono):
		self.telefono = telefono

	def set_email(self, email):
		self.email = email

#Funcion que recibe los datos que ingresa el usuario y devuelve una lista con los valores antes mencionados con el siguiente formatp "[nombre, telefono, email]"
def anadir_contacto():
	lista= []
	system("cls")
	print("\n\t\tANADIR_CONTACTO")
	print("\nIngresar el nombre: ", end="")
	lista.append(str(input()))
	print("\nIngresar telefono: ", end="")
	lista.append(int(input()))
	print("\nIngresar email: ", end="")
	lista.append(str(input()))
	return lista

#Diccionario vacio el cual se usara para guardar los contactos que el usuario ingrese
agenda = {}


while True:
	#
	system("cls")
	print("\n **************************-MENU-******************************")
	print(" *                                                            *") 
	print(" *                    1). Añadir contacto                     *") 
	print(" *                   2). Lista de contactos                   *") 
	print(" *                    3). Buscar contacto                     *") 
	print(" *                    4). Editar contacto                     *") 
	print(" *                    0). Cerrar agenda                       *") 
	print(" *                                                            *") 
	print(" **************************************************************",end="\n\n")
	decision = str(input(" Ingresar una opcion: "))
	system("cls")

	#Condicional que analiza la opcion que ingreso el usuario
	if(decision == "0"):
		break
	elif decision == "1":
		aux = anadir_contacto()
		agenda[aux[2]] = contacto(aux[0], aux[1], aux[2])
	elif decision == "2":
		for i in agenda:
			print("\n Nombre: {}".format(agenda[i].get_nombre()))
			print(" Telefono: {}".format(agenda[i].get_telefono()))
			print(" Email: {}".format(agenda[i].get_email()), end="\n\n")
			print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-")
		input("\n Ingresar cualquier valor para continuar. . . ")

	elif decision == "3":
		print("\n\t\tBUSCAR_CONTACTO")
		clave = str(input("\n Ingresar el email del contacto: "))
		print("\n Nombre: {}:".format(agenda[clave].get_nombre()))
		print(" Telefono: {}".format(agenda[clave].get_telefono()))
		print(" Email: {}".format(agenda[clave].get_email()), end="\n\n")
		input("\n Ingresar cualquier valor para continuar. . . ")
	elif decision == "4":
		print("\n\t\tEDITAR_CONTACTO")
		clave = str(input("\n Ingresar el email del contacto: "))
		print("\n\n Que desa modificar?")
		print("\n 1). Nombre")
		print("\n 2). Telefono")
		print("\n 3). Email", end="\n\n")
		decision = str(input("Ingresar una opcion: "))
		print("\n Ingresar el nuevo valor: ", end="")
		valor = ""
		if decision in "13":
			valor = str(input())
			if decision == "1":
				agenda[clave].set_nombre(valor)
			else:
				agenda[clave].set_email(valor)	
		else:
			valor = int(input())
			agenda[clave].set_telefono(valor)
		
