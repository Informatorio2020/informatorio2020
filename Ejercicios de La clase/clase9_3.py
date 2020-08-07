#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese 
#número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
#informando de ello.
#Fruta   	Precio
#Plátano		1.35
#Manzana		0.80
#Pera		0.85
#Naranja		0.70

#diccionario = {"manzana": 10, "pera": 5, "banana": 8, "naranja": 2}
diccionario= {}

while True:
	nombre = input("Ingrese el nombre de la fruta. Para salir ingrese 0")
	if nombre == "0":
		break
	precio = float(input("Ingrese el precio"))
	diccionario[nombre] = precio

fruta = input("ingrese el nombre de una fruta. Para salir ingrese N").lower()
while fruta != "n":
	kilos = input("Ingrese los kilos")
	if fruta in diccionario:
		print("El precio de la {} es {}".format(fruta, diccionario[fruta]))
		print("Total: ", int(kilos)*diccionario[fruta])

	fruta= input("ingrese el nombre de una fruta. Para salir ingrese N").lower()
