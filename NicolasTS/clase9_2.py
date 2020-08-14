#Escribí un programa que permita al usuario ingresar una frase y luego un carácter 
#(string de longitud 1) y luego muestre la frase ingresada, pero con todas las ocurrencias del 
#carácter indicado por el usuario reemplazadas por “*”. 
#"Hola Mundo"


cadena = input("ingrese una frase")
caracter = input("ingrese un caracter").lower()

#CONTROL DE STRING DE LONGITUD 1
while len(caracter) != 1:
	caracter = input("No ingresaste un caracter. Ingresalo de nuevo")

#OPCION 1
for i in cadena:
	if i.lower() == caracter:
		print("*", end = "") 
	else:
		print(i, end= "")

#OPCION 2
print("")
print(cadena.replace(caracter, "*").replace(caracter.upper(), "*"))