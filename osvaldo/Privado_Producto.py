#Definir una clase Producto, la cual debe contener los siguientes atributos publicos
# nombre, descripcion y precio y los siguientes privados, stock y codigo
#Definir el metodo mostrar_informacion() que debe mostrar el nombre, la descripcion y el precio del producto
#Metodos setter y getters para el atributo precio
#Metodos getter y setters para los atributo stock y codigo


class Producto():

	def __init__(self, nombre, descripcion, precio, stock, codigo):

		self.nombre = nombre 
		self.descripcion = descripcion
		self.precio = precio
		self.__stock = __stock
		self.__codigo = __codigo

	def mostrar_informacion(self):

		return "El nombre del producto que usted compro es: {}, la descripcion del mismo seria: {}, y su precio es de: {}".format(self.nombre, self.descripcion, self.precio)

	#Getters y Setters:

	def get_precio(self):
		return precio

	def set_precio(self, nuevo_precio):
		self.precio = nuevo_precio

	def get_stock(self):
		return stock

	def set_stock(self):
		self.__stock = __stock

	def get_codigo(self):
		return codigo

	def set_codigo(self):
		self.__codigo = __codigo

	#Primero si o si va el get 
	#El properti entra en el get para llamar y modificar al atributo 
	stock = property(get_stock, set_stock)
	codigo = property(get_codigo, set_codigo)

un_producto = Producto("Caja", "Esta es una caja comun", 123,133,1111)

print(un_producto.mostrar_informacion())

print(un_producto.get_codigo())
print(un_producto.get_stock())




#	def get_nombre(self):
#		return nombre

#	def set_nombre(self, nuevo_nombre):
#		self.nombre = nuevo_nombre

#	def get_descripcion(self):
#		return descripcion

#	def set_descripcion(self, nueva_descripcion):
#		self.descripcion = nueva_descripcion