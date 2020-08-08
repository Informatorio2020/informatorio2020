# d. En un almacén se guarda mercadería en contenedores. No es posible colocar más de n 
# contenedores uno encima del otro y, no hay área para más de 5 pilas de contenedores. 
# Elabore un programa que permita gestionar el ingreso y salida de contenedores. 
# Note que para retirar un contenedor es necesario retirar los contenedores que están
# encima de él y colocarlos en otra pila.

def NumT(n):
	A="000"+str(n)
	return A[len(A)-3:len(A)]

def MostrarContenedores(Deposito):
	os.system ("cls")
	print("\t\t",respuesta[0], " "*40)
	print("   ", end="")
	for columna in range(MaxCol[0]): print("        ", columna, end="")
	print()
	for y in range(MaxPila[0]-1, -1, -1):
		print("\t", end="")
		for x in range(MaxCol[0]):
			if Deposito[x][y] == 0: print("          ", end="")
			else: print("┌───────┐ ", end="")
		print()
		print(y, "\t", end="")
		for x in range(MaxCol[0]):
			if Deposito[x][y] == 0: print("          ", end="")
			else: print("│ ", NumT(Deposito[x][y]), " │ ", end="")
		print()
		print("\t", end="")
		for x in range(MaxCol[0]):
			if Deposito[x][y] == 0: print("          ", end="")
			else: print("└───────┘ ", end="")
		print()

def QCont():
	q=0
	for e in Deposito:
		for f in e:
			if f>0: q = q+1
	return q

def QCol(Deposito, col):
	q=0
	e=Deposito[col]
	for f in e:
		if f>0: q = q+1
	return q

def AgregarCont(Deposito, UltContenedor, MaxContenedor):
	if QCont()<MaxContenedor[0]:
		UltContenedor[0]=UltContenedor[0]+1
		for x in range(MaxCol[0]):
			for y in range(MaxPila[0]):
				if Deposito[x][y] == 0: break
			if Deposito[x][y] == 0: break
		Deposito[x][y] = UltContenedor[0]
		respuesta[0]="AGREGADO EL "+str(UltContenedor)
	else: respuesta[0]="NO HAY MAS ESPACIO"

def dondeEsta(buscado):
	for x in range(MaxCol[0]):
		for y in range(MaxPila[0]):
			if Deposito[x][y] == buscado: break
		if Deposito[x][y] == buscado: break
	if Deposito[x][y] == buscado: return(x,y)
	else: return(-1,-1)

def MoverCont(Deposito, AMover):
	Coor = dondeEsta(AMover) #Guardo la ubicación en una lista de dos elementos (Pila y ubicación)
	if Coor>=(0, 0): #Si el contenedor existe
		if Coor[1] == QCol(Deposito, Coor[0])-1: #Está arriba de todos
			c = Coor[0]+1 #La Pila que sigue a la que contiene el elemento a mover
			while c != Coor[0]:
				if c>(MaxCol[0]-1): c=0
				QcontPNew = QCol(Deposito, c) #Contenedores en la pila a mover
				if QcontPNew<MaxPila[0]: #Si hay lugar mover sino pasar a ver la siguiente pila
					(Deposito[Coor[0]][Coor[1]], Deposito[c][QcontPNew]) = (Deposito[c][QcontPNew],Deposito[Coor[0]][Coor[1]])
					respuesta[0]="MOVIDO EL CONTENEDOR "+str(AMover)
					break
				else: c=c+1
		else: respuesta[0]="NO SE PUEDE MOVER EL CONTENEDOR "+str(AMover)
	else: respuesta[0]="NO EXISTE EL CONTENEDOR "+str(AMover)

def QuitarCont(Deposito, AQuitar):
	Coor = dondeEsta(AQuitar) #Guardo la ubicación en una lista de dos elementos (Pila y ubicación)
	if Coor >= (0, 0): #Si el contenedor existe
		while Coor[1] != QCol(Deposito, Coor[0])-1:
			MoverCont(Deposito, Deposito[Coor[0]][QCol(Deposito, Coor[0])-1])
			MostrarContenedores(Deposito)
			for pausa in range(10000000): 
				pass
		Deposito[Coor[0]][Coor[1]]=0
		respuesta[0]="QUITADO EL CONTENEDOR "+str(AQuitar)
	else: respuesta[0]="NO EXISTE EL CONTENEDOR "+str(AQuitar)

def MostrarMenu(Opciones):
	print("\t", end="")
	for e in range(1,5):
		if Opciones[0] == e:
			print("┌────────────┐", end="")
		else:
			print(" "*14, end="")
	print()
	print("\t", end="")
	for e in range(1,5):
		if Opciones[0] == e:
			Separador = "│"
		else:
			Separador = " "
		print(Separador, Opciones[e], Separador, sep="", end="")
	print()
	print("\t", end="")
	for e in range(1,5):
		if Opciones[0] == e:
			print("└────────────┘", end="")
		else:
			print(" "*14, end="")
	print()

import os
from msvcrt import getch
Deposito = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
UltContenedor=[0]; MaxCol=[8]; MaxPila=[7]; MaxContenedor=[(MaxPila[0]*(MaxCol[0]-1))+1]
respuesta = [""]
Opciones = [1, "  Agregar   ", "  Mover     ", "  Quitar    ", "  Salir     "]
while True:
	MostrarContenedores(Deposito)
	MostrarMenu(Opciones)
	tecla = ord(getch())
	if (tecla == 13): #ENTER
		if Opciones[0] == 1: tecla = 65
		if Opciones[0] == 2: tecla = 77
		if Opciones[0] == 3: tecla = 81
		if Opciones[0] == 4: tecla = 83

	if (tecla == 65 or tecla == 97): #Letra A
		Opciones[0] = 1
		AgregarCont(Deposito, UltContenedor, MaxContenedor)
	elif (tecla == 77 or tecla == 109): #Letra M
		Opciones[0] = 2
		print()
		buscar = int(input("       Contenedor a MOVER: "))
		MoverCont(Deposito, buscar)
	elif (tecla == 81 or tecla == 113): #Letra Q
		Opciones[0] = 3
		print()
		buscar = int(input("       Contenedor a QUITAR: "))
		QuitarCont(Deposito, buscar)
	elif (tecla == 83 or tecla == 115): #Letra S
		Opciones[0] = 4
		break
	elif tecla == 224: #Teclas especiales
		tecla2 = ord(getch())
		if tecla2 == 75: Opciones[0] = Opciones[0]-1
		if tecla2 == 77: Opciones[0] = Opciones[0]+1
		if Opciones[0] == 0: Opciones[0] = 4
		if Opciones[0] == 5: Opciones[0] = 1

print()
print("    ┌───────────────────────────────────────────────────────────┐")
print("    │           Código compartido por José Durán                │")
print("    │           Informatorio 2020 - Comisión n°4                │")
print("    └───────────────────────────────────────────────────────────┘")
