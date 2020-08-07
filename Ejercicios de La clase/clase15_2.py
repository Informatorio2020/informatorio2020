#Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se 
#bloquee y además explica en un mensaje al usuario la causa y/o solución:
#resultado = 10/0


try:
	print(10/0)
except ZeroDivisionError:
	print("No se puede dividir por 0 ingrese otro valor")
