"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones.

    Añadir contacto

    Lista de contactos

    Buscar contacto

    Editar contacto

    Cerrar agenda
"""

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

from os import system
agenda = {}
while True:
	system("cls")
	print("\n********************************-MENU-********************************")
	print("\n1). Añadir contacto")
	print("\n2). Lista de contactos")
	print("\n3). Buscar contacto")
	print("\n4). Editar contacto")
	print("\n0). Cerrar agenda")
	print("\n**********************************************************************",end="\n\n")
	decision = str(input("Ingresar una opcion: "))
	system("cls")
	if(decision == "0"):
		break
	elif decision == "1":
		aux = anadir_contacto()
		agenda[aux[2]] = contacto(aux[0], aux[1], aux[2])
	elif decision == "2":
		for i in agenda:
			print("\n Nombre: {}:".format(agenda[i].get_nombre()))
			print("\tTelefono: {}".format(agenda[i].get_telefono()))
			print("\tEmail: {}".format(agenda[i].get_email()), end="\n\n")
			print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-")
		input("\n Ingresar cualquier valor para continuar. . . ")

	elif decision == "3":
		print("\n\t\tBUSCAR_CONTACTO")
		clave = str(input("\n Ingresar el email del contacto: "))
		print("\n Nombre: {}:".format(agenda[clave].get_nombre()))
		print(" Telefono: {}".format(agenda[clave].get_telefono()))
		print(" Email: {}".format(agenda[clave].get_email()), end="\n\n")
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
			
		else:
			valor = int(input())
		agenda[clave] = valor
		
