# Ejercicio 1
"""
from math import sqrt
def hipotenusa(lado1, lado2):
	return sqrt(lado1**2 + lado2**2)

lado1 = float(input("Ingrese primer lado: "))
lado2 = float(input("Ingrese segundo lado: "))
print("\n\nHipotenusa: {0:.2f}".format(hipotenusa(lado1, lado2)))
"""

# Ejercicio 2
"""
TARIFA_BASE = 40
TARIFA_METROS = 15

def tarifa(kilometros):
	total_metros = kilometros*1000
	return TARIFA_BASE + TARIFA_METROS * (total_metros//140)

kilometros = float(input("¿Cántos kilómetros se recorrió?\n\t"))
print("\nTarifa total: ${0:.2f}".format(tarifa(kilometros)))
"""

# Ejercicio 3
"""
ENVIO_URGENTE = 10.95
ENVIO_NORMAL = 2.95

def tarifa_envio(cantidad_elementos):
	tarifa_total = 0
	for i in range(cantidad_elementos): # Se crea un bucle for para acumular el costo por cada pedido.
		if i == 0: # A traves de esta condición solo por el primer elemento se cobrará 10.95
			tarifa_total += ENVIO_URGENTE
		else:
			tarifa_total += ENVIO_NORMAL # Todos los demás elementos que no sean el primero, acumularán un costo de $2.95 por envio
	return tarifa_total

cantidad_elementos = int(input("Cantidad de elementos del pedido:\n\t"))
print("Costo total del envíö: {0:.2f}".format(tarifa_envio(cantidad_elementos)))
"""

# Ejercicio 4
"""
def valor_medio(v1, v2, v3):
	if (v1 > v2 and v1 < v3) or (v1 > v3 and v1 < v2):
		return round(v1, 2) # Se utiliza round() en vez de formatear la salida en el print, porque sino hay problemas con con el return de la linea 51.
	elif (v2 > v1 and v2 < v3) or (v2 > v3 and v2 < v1):
		return round(v2, 2)
	elif v1 == v2 and v1 == v3:
		return "\n\nNo hay media, todos los valores son iguales\n"
	else:
		return round(v3, 2)

v1 = float(input("\nPrimer valor: "))
v2 = float(input("\nSegundo valor: "))
v3 = float(input("\nTercer valor: "))
print("El valor medio es: ", valor_medio(v1, v2, v3))
"""

# Ejercicio 5
"""
def ordinal(numero):
	global numeros
	if numero in numeros:
		return numeros[numero]
	else:
		return "" 
respuesta_control = -1

while respuesta_control != 0:
	numeros = {1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 12: "Doce"}
	print(numeros[1])
	print("Numeros del 1 al 12:\n", numeros)
	numero = int(input("Ingrese el numero entero: "))
	print(ordinal(numero))
	respuesta_control = int(input("¿Continuar? 01-SI 00-NO\n\t"))
"""

# Ejercicio 6
"""
from shutil import get_terminal_size
ancho_terminal = get_terminal_size()
ancho_terminal = ancho_terminal[0]

def centrar_string(cadena):
	return cadena.center(ancho_terminal)

cadena = input("Ingrese una cadena:\n")
print("\n\n", centrar_string(cadena))
"""

# Ejercicio 7
"""
def triangulo_valido(lado1, lado2, lado3):
	if lado1 >= (lado2 + lado3):
		return False
	elif lado2 >= (lado1 + lado3):
		return False
	elif lado3 >= (lado1 + lado2):
		return False
	else:
		return True

lado1 = float(input("Ingrese longitud del lado 1:\n"))
lado2 = float(input("Ingrese longitud del lado 2:\n"))
lado3 = float(input("Ingrese longitud del lado 3:\n"))

print("¿Es posible formar el triángulo?:\n", triangulo_valido(lado1, lado2, lado3))
"""

# Ejercicio 8

"""
def capitalizar_cadena(cadena):
	ultimo_elemento = len(cadena)-1
	cadena[0] = cadena[0].capitalize()
	for i, elemento in enumerate(cadena):
		if cadena[i] in "!.?" and i != ultimo_elemento: # Utilizo ultimo_elemento para no ejecutar el código sobre mi último elemento y evitar "index out of range".
				if cadena[i+1] == " ":
					cadena[i+2] = cadena[i+2].upper()
				else:
					cadena[i+1] = cadena[i+1].upper()

def insertar_espacios(cadena): # Se insertan espacios luego de '?, ., o !' si el usuario se olvido de hacerlo.
	ultimo_elemento = len(cadena)-1
	i = 0
	while i != ultimo_elemento: # Utilizo ultimo_elemento para "evitar index out of range" nuevamente.
		if cadena[i] in "!.?": 
			if cadena[i+1] != " ":
				cadena.insert(i+1, " ")
		i += 1

cadena = input()
cadena = list(cadena) # Convierto a lista para evaluar caracter por caracter y poder modificar las minúsculas.
insertar_espacios(cadena) 
capitalizar_cadena(cadena)
print(cadena)
cadena = "".join(cadena) # Transformo la lista en una string, sin usar ningun separador porque ya utilicé insertar_espacios(cadena).
print(cadena)
"""

# Ejercicio 9

def mi_funcion(algo=None):
	try:
		if algo is None:
			raise ValueError("Error! No se permite un valor nulo")
	except ValueError:
		print("Error! No se permite un valor nulo (desde la excepción)")

mi_funcion(None)
