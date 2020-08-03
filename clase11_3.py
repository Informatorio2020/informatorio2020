#En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento 
#dependiendo de un número que se escoge al azar. 
#Si el número escogido 
#es menor que 50 el descuento es del 15% sobre el total de la compra, 
#si es mayor o igual a 50 el descuento es del 20%. 
#si el numero es mayor a 100 calcule el 30%
#Obtener cuánto dinero se le descuenta.
#El programa se debe ejecutar hasta que ingrese un total de compra igual a 0

print("Este programa hace calculos de descuento")


total = float(input("Ingrese el monto de la compra. Para salir ingrese 0"))

while total != 0:
	numero = int(input("Ingrese un numero"))
	if numero < 50:
		descuento = total * 0.15
	elif numero >= 50 and numero < 100:
		descuento = total * 0.2
	elif numero > 100:
		descuento= total * 0.3
	print("El descuento es de: ", descuento)
	descuento = 0

	total = float(input("Ingrese el monto de la compra. Para salir ingrese 0"))
	



print("Fin del programa")