"""Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, 
almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que 
indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la 
misma letra. Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que
 ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya 
 que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará 
 False, ya que no coinciden ni la primera ni la última letra. """

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