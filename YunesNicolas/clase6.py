#Crea un diccionario donde la clave sea el nombre del usuario y el
#valor sea el teléfono. Tendrás que ir pidiendo contactos hasta el usuario 
#diga que no quiere insertar más. No se podrán almacenar nombres repetidos.


dic={}

control = input("MENU:\n1: Agregar registro\n0: Termina el programa")

while control == "1":
	nombre= input("Ingrese un nombre")
	telefono= input("Ingrese un telefono")

	

	if nombre in dic.keys():
		opcion = input("El contacto ya existe. Quiere editar el numero?. S/N")
		if opcion.upper() == "S":
			dic.update({nombre: telefono})
	else:
		dic.update({nombre: telefono})
	
	
	print("MENU:")
	print("1: Agregar registro")
	print("0: Termina el programa")

	control = input()


print("DICCIONARIO: ", dic)