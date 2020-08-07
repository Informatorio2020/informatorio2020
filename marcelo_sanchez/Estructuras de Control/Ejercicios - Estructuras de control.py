# EJERCICIO 1: Edad de una persona
"""
edad = int(input("Ingrese la edad de la persona: "))

if edad >= 18:
	print("Es mayor de edad")
else:
	print("Es menor de edad") 
"""

# EJERCICIO 2: Porcentajes de las encuestas
"""
preguntas = int(input("Ingrese la cantidad de preguntas realizadas: "))
respuestas = int(input("Ingrese la cantidad de respuestas corectas: "))
porcentaje = (respuestas/preguntas)*100

if porcentaje >= 90:
	print("Resultado: EXCELENTE")
elif porcentaje >= 70:
	print("Resultado: BUENO")
elif porcentaje >= 60:
	print("Resultado: APROBADO")
else:
	print("Resultado: DESAPROBADO")
"""

#  EJERCICIO 3: Login de usuario. 
"""
contador = 0
pass_correcta = 123


while contador <= 5:
	usuario = input("Ingrese un usuario: ")
	_pass = int(input("Ingrese su contraseña: "))
	if _pass == pass_correcta:
		print("Ha iniciado sesion correctamente")
		break
	else:
		contador += 1
		print("Intente nuevamente")
		print()

if contador > 5:
	print("CUENTA BLOQUEADA.")
"""

# EJERCICIO 4: VENTAS dia 1 y dia 2
"""
ventas_dia1 = int(input("Ingrese las ventas del dia 1: "))
print()
ventas_dia2 = int(input("Ingrese las ventas del dia 2: "))
print()

if ventas_dia1 > ventas_dia2:
	print("Se vendio mas el dia 1")
elif ventas_dia1 == ventas_dia2:
	print("Se vendio la misma cantidad en ambos dias")
else:
	print("Se vendio mas el dia 2")
"""

# EJERCICIO 5: Pizza Vegetariana o no.
"""
pizza_vegetariana = input("Desea una pizza vegetariana? Responda SI o NO: ")
print()

if pizza_vegetariana == "SI":
	ingredientes = input("Elija un ingrediente: RUCULA o PIMIENTO: ")
	print()
	print("PIZZA ELEGIDA: Vegetariana.")	
	if ingredientes == "RUCULA":
		print("Ingredientes: Mozarella, tomate y rucula.")
	else:
		print("Ingredientes: Mozarella, tomate y pimiento.")
		print()
else:
	ingredientes = input("Elija un ingrediente: JAMON o PANCETA: ")
	print()
	print("PZZA ELEGIDA: No vegetariana.")
	if ingredientes == "JAMON":
		print("Ingredientes: Mozarella, tomate y jamon.")
	else:
		print("Ingredientes: Mozarella, tomate y panceta.")

"""

# EJERCICIO 6: Grupos A y B.

nombre = input("Ingrese su nombre: ")
nombre = nombre.lower() # Con el metodo lower() convierto el string a minusculas, para manejar los codigos ASCII de las minusculas.
turno = input("Ingrese su turno (tarde o noche): ")
nombre = ord(nombre[0]) # El metodo ord() en este caso devuelve el codigo ASCII del caracter 0 del string y lo guardo en nombre.
posicion_m = ord('m') # De nuevo se guarda el codigo ASCII del caracter m, para utilizarlo luego en los condicionales. Lo guardo en la varable.

# En cada caso condicional, comparo el codigo ASCII del primer caracter con el codigo de la 'm'.
if (nombre <= posicion_m) and turno == "tarde":
	print("GRUPO: A")
elif (nombre > posicion_m) and turno == "noche":
	print("GRUPO: A")
elif (nombre <= posicion_m) and turno == "noche":
	print("GRUPO: B")
elif (nombre > posicion_m) and turno == "tarde":
	print("GRUPO: B")
else:
	print("ERROR. Ingrese sus datos de nuevo.")



