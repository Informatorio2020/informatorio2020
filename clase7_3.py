#Realiza una función llamada relacion(a) y que va a pedir un numero 
#a partir de dos números cumpla lo siguiente:
#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.



def relacion():
	a= int(input("Ingrese un numero"))
	b= int(input("Ingrese un numero"))
	if a > b:
		print("1")
	elif a < b:
		print("-1")
	else:
		print("0")

relacion()
relacion()
relacion()