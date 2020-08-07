"""
En este archivo se encuentran (en desarrollo) todos los desafíos de los tres niveles: 
Stone, Silver y SUper Sayayin de POO. Cada caso está comentado con comillas triples 
al inicio y al final de cada código. 
"""
#Ejercicio 1
# Clase cuenta, atributos: titular y cantidad (puede tener decimales)
# El titular sera obligatoirto y la cantidad es opcional, crear constructor.
"""
class Cuenta():
	def __init__(self, titular, cantidad=0):
		self.titular = titular
		self.cantidad = cantidad

	def obtener_informacion(self):
		print("Titular: ", self.titular)
		print("Cantidad: ", self.cantidad)

	def modificar_informacion(self, titular, cantidad):
		self.titular = titular
		self.cantidad = cantidad

	def ingresar_cantidad(self, cantidad):
		if cantidad > 0:
			self.cantidad += cantidad

	def retirar_cantidad(self, cantidad):
		if self.cantidad - cantidad > 0:
			self.cantidad -= cantidad
		else:
			self.cantidad = 0


cuenta1 = Cuenta("ABC", 55)
cuenta1.obtener_informacion()
cuenta1.modificar_informacion("Marcelo", 100)
cuenta1.ingresar_cantidad(200)
cuenta1.obtener_informacion()
cuenta1.retirar_cantidad(3300)
cuenta1.obtener_informacion()

print(type(Cuenta))
print(Cuenta)
print(Cuenta.__name__)
"""
# Promedio de todos los cursos de una escuela
"""
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)


    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO\n\n")


juan = Cliente(405555, "Juan", "Sanchez")
hector = Cliente(2323434, "Hector", "Gutierrez")
fernando = Cliente(23424, "Fernando", "Cavenaghi")
empresa = Empresa([juan, hector, fernando])
print("Listado de clientes:\n\n")
empresa.mostrar_cliente(2323434)
empresa.mostrar_cliente(23424)
print("\n\n")
empresa.borrar_cliente(23424)
print(juan)
print(empresa)
"""
"""
class Producto():

	def __init__(self, nombre, descripcion, precio, stock, codigo):
		self.nombre = nombre
		self.descripcion = descripcion
		self.precio = precio
		self.__stock = stock
		self.__codigo = codigo

	def mostrar_informacion(self):
		return "Nombre: {}\nDescripcion: {}\nPrecio: {}\n".format(self.nombre, self.descripcion, self.precio)

	def get_precio(self):
		return self.precio

	def set_precio(self, precio):
		self.precio = precio

	def get_stock(self):
		return self.stock

	def set_stock(self, cantidad_stock):
		self.__stock = cantidad_stock

	def get_codigo(self):
		return self.__codigo

	def set_codigo(self, codigo):
		self.__codigo = codigo

	precio = property(get_precio, set_precio)
	stock = property(get_stock, set_stock)
	codigo = property(get_codigo, set_codigo)


harina = Producto("Oreo", "Galletitas dulces", 90, 120, "ABC234")
print(harina.mostrar_informacion())
print("Precio: {}\n".format(harina.get_precio()))
print("Stock: {}\n".format(harina.get_stock()))
print("Codigo: {}\n".format(harina.get_codigo))
"""

# DESAFIOS LEVEL STONE
# Caso 1 y 2
"""
class Vehiculo():

	def __init__(self, color, cantidad_ruedas = 2):
		self.color = color
		self.ruedas = cantidad_ruedas


class Coche(Vehiculo):

	def __init__(self, color, velocidad, cilindrada, cantidad_ruedas = 2):
		Vehiculo.__init__(self, color, cantidad_ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada


class Bicicleta(Vehiculo):

	def __init__(self, color, tipo, cantidad_ruedas = 2):
		Vehiculo.__init__(self, color, cantidad_ruedas)
		self.tipo = tipo


class Motocicleta(Bicicleta):

	def __init__(self, color, tipo, velocidad, cilindrada, cantidad_ruedas = 2):
		Bicicleta.__init__(self, color, tipo, cantidad_ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada


class Camioneta(Coche):

	def __init__(self, color, velocidad, cilindrada, carga, cantidad_ruedas = 2):
		Coche.__init__(self, color, velocidad, cilindrada, cantidad_ruedas)
		self.carga = carga


def catalogar(lista_vehiculos, ruedas = 0):
	contador_vehiculos = 0
	for vehiculo in lista_vehiculos:
		if vehiculo.ruedas == ruedas:
			contador_vehiculos += 1
			atributos = vars(vehiculo) # retorna un diccionario donde las keys son los atributos y los values los valores de dicho atributo
			print("\n", type(vehiculo).__name__)
			for item in atributos:
				print(item, ":", atributos[item])
	print("\nSe han encontrado {} vehiculos con {} ruedas".format(ruedas, contador_vehiculos))
			
coche = Coche("Rojo", 180, 3, 4)
bicicleta = Bicicleta("Verde", "Deportiva", 2)
motocicleta = Motocicleta("Negro", "Urbana", 120, 110, 2)
camioneta = Camioneta("Amarillo", 200, 5, 200, 4)
vehiculos = [coche, bicicleta, motocicleta, camioneta]
parametro_ruedas = int(input("Cantidad de ruedas para filtrar la búsqueda: "))
catalogar(vehiculos, parametro_ruedas)
"""

# Caso 3
"""
class Triangulo():

	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def mayor_lado(self):
		mayor = max(self.lado1, self.lado2, self.lado3)
		return mayor

	def tipo_triangulo(self):
		tipo_triangulo = ""
		if self.lado1 == self.lado2 and self.lado1 == lado3:
			tipo_triangulo = "Equilátero\n\n"
		elif (self.lado1 == self.lado2 and self.lado1 != lado3) or (self.lado1 == self.lado3 and self.lado1 != self.lado2):
			tipo_triangulo = "Isósceles\n\n"
		else:
			tipo_triangulo = "Escaleno\n\n"

		return tipo_triangulo

lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))
triangulo = Triangulo(lado1, lado2, lado3)
print("El lado más grande es: {}\n".format(triangulo.mayor_lado()))
print("Tipo de triángulo: {}\n".format(triangulo.tipo_triangulo()))
"""

# Caso 4
"""
from shutil import get_terminal_size

class Agenda():

	def __init__(self, contacto=[]):
		self.contactos = contacto

	def mostrar_contactos(self):
		for contacto in self.contactos:
			print(contacto.nombre, contacto.apellido)

	def buscar_contacto(self, nombre, apellido):
		datos_contacto = "Contacto no encontrado"
		for i in range(len(self.contactos)): # TypeError: cannot unpack non-iterable Contacto object
			if self.contactos[i].nombre == nombre and self.contactos[i].apellido == apellido:
				datos_contacto = i
		return datos_contacto # Retorno la posición del objeto en la lista de self.contacto

	def agregar_contacto(self, contacto):
		self.contactos = contacto


class Contacto():

	def __init__(self, nombre, apellido, numero):
		self.nombre = nombre
		self.apellido = apellido
		self.numero = numero

	def __str__(self):
		return "\n\nNombre y Apellido: {} {}\nNumero: {}\n\n".format(self.nombre, self.apellido, self.numero)

	def editar_contacto(self, nombre, apellido, numero):
		self.nombre = nombre
		self.apellido = apellido
		self.numero = numero


def agregar_contacto_funcion(agenda, lista_contactos = []):
	while True:
		nombre = input("Escriba un nombre: ")
		apellido = input("Escriba un apellido: ")
		numero = input("Escriba un número: ")
		contacto = Contacto(nombre, apellido, numero)
		lista_contactos.append(contacto)
		respuesta = int(input("¿Continuar agregando? 01-SI 00-NO\n\t"))
		if respuesta == 0:
			break



def buscar_contacto_funcion(agenda):
	nombre_busqueda = input("Nombre del contacto requerido:\t")
	apellido_busqueda = input("\nApellido del contacto requerido:\t")
	contacto_encontrado = agenda.buscar_contacto(nombre_busqueda, apellido_busqueda)
	return contacto_encontrado


# Interfaz del tipo menu
ancho_terminal = get_terminal_size() # Funcion que retorna una tupla, con el ancho y alto de la terminal.
ancho_terminal = ancho_terminal[0] # Guardo solo el ancho de la terminal, para centrar el mensaje.
agenda_marcelo = Agenda()
lista_contactos = []

print("MENÚ DE GESTIÓN DE LA AGENDA".center(ancho_terminal))
while True:
	print("Elija una opción (o 5 para cerrar la agenda):\n")
	opcion = int(input("\n01-Agregar contacto\n02- Lista de contactos \n03- Buscar contacto\n04- Editar contacto\n05- Cerrar agenda\n\n"))
	if opcion == 1:
		agregar_contacto_funcion(agenda_marcelo, lista_contactos)
		agenda_marcelo.agregar_contacto(lista_contactos)
	elif opcion == 2:
		agenda_marcelo.mostrar_contactos()
	elif opcion == 3:
		pos_contacto = buscar_contacto_funcion(agenda_marcelo) 
		print(agenda_marcelo.contactos[pos_contacto])
	elif opcion == 4:
		pos_contacto = buscar_contacto_funcion(agenda_marcelo)
		nombre_editado = input("Editar nombre:\t")
		apellido_editado = input("Editar apellido:\t")
		numero_editado = int(input("Editar número:\t"))
		agenda_marcelo.contactos[pos_contacto].editar_contacto(nombre_editado, apellido_editado, numero_editado) # Edito el contacto en la pos_contacto específica de la lista.
	elif opcion == 5:
		print("AGENDA CERRADA".center(ancho_terminal))
	else:
		print("Opcion incorrecta, intente de nuevo.\n\n")

	if opcion == 5:
		break

print("\n\n Tipo de objeto de agenda_marcelo.contactos:\n\n{}".format(type(agenda_marcelo.contactos)))
"""

# Caso 5
"""
class Tiempo():

	def __init__(self, hora, minutos = 00, segundos = 00):
		self.__hora = hora
		self.__minutos = minutos
		self.__segundos = segundos

	def get_hora(self):
		return "{}:{}:{} hs\n".format(self.hora, self.minutos, self.segundos)

	def set_hora(self, hora, minutos = self.minutos, segundos = self.segundos):
		self.__hora = hora
		self.__minutos = minutos
		self.__segundos = segundos

	hora = priority(get_hora, set_hora)


class PruebaTiempo():

	def __init__(self, objeto_tiempo):

"""

# LEVEL SILVER
# Caso 1 - Pizzeria

class Pizza():

	def __init__(self, tamanio = 8, ingredientes, tipo_coccion):
		self.__tamanio = tamanio
		self.__ingredientes = ingredientes
		self.__tipo = tipo_coccion

	def get_tipo(self):
		return self.tipo

class Calabrese(Pizza):
	pass

class Muzzarella(Pizza):
	pass


class Calabrese(Pizza):
	pass


class Fugazzeta(Pizza):
	pass


class Napolitana(Pizza):
	pass


