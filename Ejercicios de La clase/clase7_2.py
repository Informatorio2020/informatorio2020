#Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.


def relacion(a=0,b=0):
	if a > b:
		comparacion= 1
	elif a < b:
		comparacion= -1
	else:
		comparacion= 0
	return comparacion

variable= relacion(b=5, a=7)
print(relacion(10, 4))
operacion = relacion(5, 5) + relacion(5)
print(operacion)
print(variable)