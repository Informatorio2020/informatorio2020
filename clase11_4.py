#Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. 
#Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, 
#tomando en cuenta lo siguiente:
#El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
#El programa finaliza cuando se introduce una D como tipo de gasolina.
precio = {"A": 50, "B":55, "C":60}
litrosA=0 
litrosB=0 
litrosC=0

tipo = input("Que tipo de combustible compro A, B o C. Para salir ingrese D").upper()

while tipo != "D":
	if tipo not in precio:
		tipo = input("Que tipo de combustible compro A, B o C. Para salir ingrese D").upper()
		continue

	combustible = float(input("Cuanto combustible compro"))

	precio_total = combustible * precio[tipo]

	print("Precio: ", precio_total)

	if tipo == "A":
		litrosA = litrosA + combustible
	elif tipo == "B":
		litrosB = litrosB + combustible
	elif tipo== "C":
		litrosC = litrosC + combustible

	tipo = input("Que tipo de combustible compro A, B o C. Para salir ingrese D").upper()



print("Litros de A: ", litrosA)
print("Litros de B: ", litrosB)
print("Litros de C: ", litrosC)