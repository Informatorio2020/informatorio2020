#Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, 
# los cuales pueden aparecer repetidos en la lista, si tienen registrado más de un número 
# telefónico. La compañía para su próximo aniversario desea enviar un regalo a sus clientes,
#  sin repetir regalos a un mismo cliente. En una lista se almacenan los regalos disponibles 
#  en orden. Se desea un programa que cree una nueva lista con los clientes, sin repetir
#  y ordenada. 
#Se desea un programa que cree una nueva lista con los clientes, sin repetir
#  y ordenada. Y que al final muestre el regalo que le corresponde a cada cliente.


lista = [["Juan", 12223],["Juan",4566576], ["Ana", 95679856], ["Maria", 5468965], ["Ana", 467578], ["Mariana", 3445]]
regalos = ["Regalos1", "Regalos2"]

resultado = []

for i in lista:
	if i[0] not in resultado:
		resultado.append(i[0])

resultado.sort()

indice = 0

print(resultado)

for i in range(len(resultado)):
	print("Al cliente {} le corresponde {} regalo".format(resultado[i], regalos[indice]))
	indice = indice +1 if indice< 1 else 0

