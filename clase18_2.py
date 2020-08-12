#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales).
#El titular será obligatorio y la cantidad es opcional. Crea el constructor que cumpla lo anterior.

class Cuenta():

	def __init__(self, cualquier_cosa, cantidad=None):
		self.titular = cualquier_cosa
		self.cantidad = cantidad
		self.datos_de_la_cuenta = titular + str(cantidad)

#Crea sus métodos:
#obtener_informacion()
	def obtener_informacion(self):
		return self.datos_de_la_cuenta


#modificar_informacion()
	def modificar_nombre_titular(self, nombre):
		self.titular = nombre

	#Metodo 
	def retirar(self, cantidad):
		#Modifica el valor del atributo cantidad del objeto
		self.cantidad = self.cantidad - cantidad
		if self.cantidad < 0:
			self.cantidad = 0


Objeto1 = Cuenta("Mariana", 1000)
print(Objeto1.obtener_informacion())


Objeto2 = Cuenta("Paula", 3000)
print(Objeto2.obtener_informacion())



#Tendrá dos métodos especiales:
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
#negativa, no se hará nada.




#retirar( cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que 
#nos pasan es #negativa, la cantidad de la cuenta pasa a ser 0.
