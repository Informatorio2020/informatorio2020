#Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se
#bloquee y además explica en un mensaje al usuario la causa y/o solución:
#lista = [1, 2, 3, 4, 5]
#lista[10]


try:
	lista = [1, 2, 3, 4, 5]
	lista[10]
except IndexError:
	print("El indice no se encuentra en la lista. Los indices deben ser entre 0 y {}".format(len(lista)-1))
