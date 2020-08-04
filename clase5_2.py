

acumulador= 0

contador = 0

control = 3

nota = int(input("ingrese una nota"))
auxiliar =nota 

while nota > 0:
	acumulador = acumulador + nota
	control -= 1
	contador +=  1
	print(control)	
	if nota > auxiliar:
		auxiliar = nota

	nota = int(input("ingrese una nota"))



print("Contador de iguales", control)
print("la suma de las notas es ", acumulador)
print("el promedio ", round(acumulador/contador, 2))
print("la nota mayor es", auxiliar)