""" Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.
    Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.
    Modifica la función catalogar() para que reciba un argumento optativo ruedas
    haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
    También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas.
    Ponla a prueba con 0, 2 y 4 ruedas como valor."""


class Vehiculo:
    vehiculo = []
    cantidad = 0
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    Vehiculo.vehiculos.append(self)
    Vehiculo.cantidad =+ 1

    @staticmethod
    def catalogar(ruedas= 2):
        for item in Vehiculo.vehiculos:
          print("Atributos: ",item, ". Clase: ", type(item).__name__)


class Coche(Vehiculo):
    def __init__ (self,velocidad,cilindrada,color,ruedas):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
      return "{}, {}, {}, {}".format(self.velocidad, self.cilindrada, self.color, self.ruedas)


class Camioneta(Coche):
    def __init__(self,velocidad,cilindrada,color,ruedas,carga):
        super().__init__(velocidad,cilindrada,color,ruedas)
        self.carga = carga
    
    def __str__(self):
      return "{}, {}, {}, {}, {}".format(self.velocidad, self.cilindrada, self.color, self.ruedas, self.carga)


class Bicicleta(Vehiculo):
    def __init__(self,tipo,color,ruedas):
        self.tipo = tipo
        super().__init__(color,ruedas)
    
    def __str__(self):
      return "{}, {}, {}".format(self.tipo, self.color, self.ruedas)

class Motocicleta(Bicicleta):
  def __init__(self, velocidad, cilindrada, tipo,color,ruedas):
    self.velocidad= velocidad
    self.cilindrada= cilindrada
    super().__init__(tipo,color,ruedas) 
  
  def __str__(self):
     return "{}, {}, {}, {}".format(self.velocidad, self.cilindrada, self.tipo, self.color, self.ruedas)


nissan = Camioneta('180','2.0 turbo', 'Negro', '4', '1100') 
print(nissan.carga)
print(nissan.color)