#crear una clase llamada Cuenta que tendra los siguientes atributos: Titular y cantidad (puede tener decimales)
#El titular sera obligatorio y la cantidad es opcional. crea el constructor que cumpla con lo anterior

class Cuenta():
    def __init__(self, titular, cantidad= None):
        self.titular = titular
        self.cantidad = cantidad
        self.datos_cuenta = titular + str(cantidad)

#Crea sus metodos
#obtener informacion
#modificiar informacion

    def get_info(self):
        return self.datos_cuenta

    def modificar_informacion(self, titular):
        self.titular = titular

#Tendra dos metodos especiales:
#Ingresar (Cantidad): Se ingresa una cantidad a la cuenta, si la cantidad es negativa, no se hara nada
#retirar (cantidad): Se retira una cantidad a la cuenta, si ingresando la cantidad actual a la que nos pasan es negativa
#La cantidad pasa a ser 0.

    def ingresar_cantidad(self, cantidad):
        self.cantidad = self.cantidad + cantidad
        if cantidad < 0:
            self.cantidad+= cantidad


    def retirar(self, cantidad):
        self.cantidad = self.cantidad + cantidad
        if cantidad < 0:
            self.cantidad = 0

cuenta1 = Cuenta('Max', '45.000')

#cuenta1.ingresar_cantidad(15.000)
#cuenta1.retirar()
#cuenta1.modificar_informacion('Mara')
#cuenta1.get_info()

#print(cuenta1)