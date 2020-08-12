#Definir la clase Persona con los atributos nombre(privado) y edad(publico)
#Definir los getter y setter de cada uno
#Definir un metodo mostrar_info que muestre el nombre y la edad de la persona

#atributos protegidos y privados
# UN guion bajo -> protegido, te avisa que es protegido, pero podes acceder y modificar
# DOS guion bajo -> privado, no te deja ni acceder, ni modificar

class Persona():
    def __init__(self, nombre, edad):
        self.__un_nombre = nombre
        self.una_edad = edad
    
    def get_nombre(self):
        return self.__un_nombre

    def get_edad(self):
        return self.una_edad
    
    def set_nombre(self, nombre):
        self.__un_nombre = nombre
    
    def set_edad(self, edad):
        self.una_edad = edad

    def _mostrar_info(self):
        return "Nombre: {}. Edad: {}.".format(self.__un_nombre, self.una_edad)

una_persona = Persona("juan", 18)

print(una_persona._mostrar_info())


#Definir una clase Producto, la cual debe contener los siguientes atributos publicos
# nombre, descripcion y precio y los siguientes privados, stock y codigo
#Definir el metodo mostrar_informacion() que debe mostrar el nombre, la descripcion y el precio del producto
#Metodos setter y getters para le atributo precio
#Metodos getter y setters para los atributo stock y codigo

class Producto():
    def __init__(self, nombre, descripcion, precio, stock, codigo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.__stock = stock
        self.__codigo = codigo

    def mostrar_informacion(self):
        return "Nombre: {}. Descripción: {}. Precio: {}.".format(self.nombre, self.descripcion, self.precio)

    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

    def get_stock(self):
        return self.__stock

    def get_codigo(self):
        return self.__codigo
    
    def set_stock(self, stock):
        self.__stock = stock
    
    def set_codigo(self, codigo):
        self.__codigo
    
    stock = property(get_stock, set_stock)
    codigo = property(get_codigo, set_codigo)

un_producto = Producto("caja", "esta es una caja común",20.50,133,1111)

print(un_producto.mostrar_informacion())

print(un_producto.get_codigo())

print(un_producto.get_stock())