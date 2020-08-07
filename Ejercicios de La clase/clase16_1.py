#3
#Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, 
#capturar las excepciones ZeroDivisionError y ValueError.

try:
	primer_numero= int(input("Ingrese un numero"))
	segundo_numero = int(input("Ingrese el segundo numero"))
	print(primer_numero/segundo_numero)
except ZeroDivisionError:
	print("No se puede hacer una division por 0")
except ValueError:
	print("Se lanzo un excepcion de tipo ValueError")
except Exception:
	print("Otro tipo de error")


#4
#Realizar la carga de dos números por teclado e imprimir la división del primero
#respecto al segundo. Capturar cualquier tipo de excepción que se dispare.

try:
	primer_numero= int(input("Ingrese un numero"))
	segundo_numero = int(input("Ingrese el segundo numero"))
	print(primer_numero/segundo_numero)
except Exception:
	print("Se lanzo una excepción")
