#Ejercicio 2:
#Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número
#de mes y mostrar seguidamente el nombre de dicho mes. Capturar la excepción IndexError.

tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre")

try:
	mes=int(input("Ingrese número de mes: "))
	if mes < 1:
		raise IndexError
	print(tupla[mes-1])

except IndexError:
	print("ESTAMOS HABLANDO DE 1 A 12...QUE PUSISTE?")