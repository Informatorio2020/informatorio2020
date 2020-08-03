#En un almacén se guarda mercadería en contenedores. 
#No es posible colocar más de n contenedores uno encima
#del otro y, no hay área para más de 5 pilas de contenedores. 
#Elabore un programa que permita gestionar el
#ingreso y salida de contenedores. 
#Note que para retirar un contenedor es necesario retirar los contenedores
#que están encima de él y colocarlos en otra pila.
#completa primero una pila
#una pila para mover
#si esta lleno solo permite retirar
#n = 3 


def guardar(contenido):
	#GUARDAR los contenedores
	#Recorro la lista de contenedores
	global almacen

	for indice in range(len(almacen)-1):
		if len(almacen[indice])<3:
			almacen[indice].append(contenido)
			break
		else:
			print("Almacen esta lleno")



def recuperar(identificador):
	#Recuperar un contenedor de alguna de las listas
	global almacen

	for pila in almacen:
		
		if identificador in pila:
			for indice in range(len(pila)-1,-1,-1):
				print("-----",pila[indice])
				if identificador == pila[indice]:
					#Encontramos lo que estabamos buscando
					print("El elemento buscado estaba en la posicion {} de la pila".format(indice))
					del pila[indice]
					print(almacen[4])
					for indice2 in range(len(almacen[4])-1,-1,-1):
						#Se encarga de devolver los contenedores al origen
						pila.append(almacen[4][indice2])
						del almacen[4][indice2]
					break

				else:
					#desapilar
					almacen[4].append(pila[indice])
					del pila[indice]

			break


almacen=[[3,2,56],[4,3,],[4,7,56],[34,67,78],[8,7]]



n=3

contenido = int(input("ingrese el contenido"))

guardar(contenido)

print(almacen)

identificador = int(input("Ingrese el identificador del elemento a eliminar"))

recuperar(identificador)

print(almacen)

#Mostrar las pilas verticales
#for i in range(n):  						
#	for pila in range(5, 0):					
#		print(almacen[pila][i], end="   ")
#	print("")



