
class Aula():

	#Constructor de la clase Aula
	def __init__(self, profesor, alumnos=0):
		self.nombre_del_profesor = profesor
		self.cantidad_de_alumnos = alumnos
		self.nombre_del_curso = "Sin nombre"
		self.horas = 100
		print("Se creo un nuevo objeto de la clase Aula, que dura {}".format(self.horas))


	#Metodo que le permite modificar el nombre del curso
	def modificar_nombre_del_curso(self, nombre):
		self.nombre_del_curso = nombre


#Crear una instancia de la clase
clase_virtual1 = Aula("Mariana")

clase_virtual1.modificar_nombre_del_curso("Clase programacion web")

print("Modifica desde una funcion: ", clase_virtual1.nombre_del_curso)

clase_virtual1.nombre_del_curso= "Clase virtual de programacion web"

print("Modificado directamente: ", clase_virtual1.nombre_del_curso)

class Mesa:
	def __init__(self, color, tamano):
		self.color= color
		self.tamano= tamano

	def __str__(self):
		return "Esta es una mesa de color {} y de tamaño {}".format(self.color, self.tamano)


mesa = Mesa("blanca", "mediana")
print(mesa.tamano)
print(mesa)

mesa2 = Mesa("marron", "grande")
print(mesa2.tamano)
print(mesa2)

mesa3 = Mesa("Negro", "chico")
print(mesa3.tamano)
print(mesa3)

























