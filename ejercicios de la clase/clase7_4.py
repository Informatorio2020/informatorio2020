#Realiza una función llamada area_circulo(radio) que devuelva el área de un 
#círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

#Realizar una funcion que calcule el area de un cuadrado



def area_circulo(radio):
	return radio ** 2 * 3.14159

rad=int(input("Ingrese el radio: "))

area = area_circulo(rad)

print(round(area,3))

def area_cuadrado(lado):
	print("area cuadrado", lado**2)

lado = int(input("Ingrese el valor del lado"))
area_cuadrado(lado)