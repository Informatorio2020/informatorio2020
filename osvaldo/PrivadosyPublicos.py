class Persona():

	def __init__(self, __nombre, _edad):

		self.__nombre = __nombre
		self._edad = _edad
		self.sueldo = 100

	#Metodos Getters y Setters:

	def set_edad(self, nueva_edad):

		print("Estoy en el set de edad")
		self._edad = nueva_edad

	def get_edad(self):

		print("Estoy en el set de edad")
		return self._edad

	#Nombre
	def set_nombre(self, nuevo_nombre):

		print("Estoy en el set de nombre")
		self.__nombre = nuevo_nombre

	def get_nombre(self):

		print("Estoy en el getter de nombre")
		return self.__nombre

	def sueldos():
		print(self.sueldo)
	#Si yo no quiero mostrar lo que esta adentro de este metodo tengo que ponerle 
	#dos barras __ a mostrar 
	def __mostrar_info(self):

		return "La persona {} tiene {} años".format(self.__nombre, self.edad) 

	def publico(self):
		return self.__mostrar_info()

	##Este metodo me va a permitir Modificar el nombre ya que entra en el geter y el seter

	nombre = property(get_nombre, set_nombre)	
	edad = property(get_edad, set_edad)

persona1 = Persona("Ana", 34)
print(persona1.nombre)
persona1.nombre = "Pedro con el metodo"


print(persona1.edad)

persona1.sueldos()

#print(persona1.get_nombre())
#persona1.__nombre = "Otra Cosa"
#print(persona1.__nombre)
#print(persona1.get_nombre())

##print(persona1.mostrar_info())
#print(persona1.publico())

