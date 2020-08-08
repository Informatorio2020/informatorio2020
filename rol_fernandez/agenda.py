#AGENDA USANDA LA FUNCION DICCIONARIO
agenda=dict()
agenda={"nombre": "telefono"}

print ("Para guardar un registro ingrese G. \nPara eliminar un registro ingrese D. \n Para editar un registro ingrese E. \n")
control = input().upper()

while control != "N":
	if control == "G":
#guardar
		nombre= input ("Ingrese nombre: ")
		if nombre in agenda:
			print ("El nombre ya esta agendado")
		telefono= input("Ingrese el numero de telefono: ")

		agenda[nombre]= telefono
		print(agenda)
	elif control == "D":
#eliminar
		nombre=input("Ingrese nombre: ")
		del agenda[nombre]
		print(agenda)

	elif control == "E":	
#editar el registro de una agenda
		nombre=input("Ingrese nombre: ")
		print ("El número actual es: ", agenda[nombre])
		telefono= input("Ingrese el numero de telefono")
		agenda[nombre]= telefono
		print(agenda)

	print ("Para guardar un registro ingrese G. \nPara eliminar un registro ingrese D. \n Para editar un registro ingrese E. \n")
	control = input().upper()