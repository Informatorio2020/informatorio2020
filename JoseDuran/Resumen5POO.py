'''CASO 1
   A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.
  Vehículo
    color
    ruedas
      |
  Coche
    velocidad (km/h)
    cilindrada (cc)

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
  def __init__(self, color, ruedas, velocidad, cilindrada):
    Vehiculo.__init__(self, color, ruedas)
    self.cilindrada = cilindrada
    self.velocidad = velocidad

coche1 = Coche("Rojo", 4, 200, 1800)
print(coche1.color)
print(coche1.ruedas)
print(coche1.velocidad)
print(coche1.cilindrada)
'''

'''CASO 2
> Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.
> Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra 
mostrando el nombre de su clase y sus atributos.
> Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo 
que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente 
si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
  Vehículo
    color
    ruedas
     |
  Coche
    velocidad (km/h)
    cilindrada (cc)
     |
  Camioneta
    carga (kg)

class Vehiculo():
  vehiculos=[]
  def __init__(self, color, ruedas):
      self.color = color
      self.ruedas = ruedas
      Vehiculo.vehiculos.append(self)

  def catalogar(vehcls, rueds = None):
    cantVe = 0
    print("-"*70)
    for e in vehcls:
      if (rueds is None) or (e.ruedas == rueds):
        cantVe += 1
        print(type(e).__name__, "\t\t", e)
    print("-"*70)
    print("Total de vehículos:", cantVe)

class Coche(Vehiculo):
  def __init__(self, color, velocidad, cilindrada):
    Vehiculo.__init__(self, color, 4)
    self.velocidad = velocidad
    self.cilindrada = cilindrada
  def __str__(self):
    return (" Color: {} Ruedas: {} Velocidad: {} Cilindrada: {}".format(self.color, self.ruedas, self.velocidad, self.cilindrada))

class Camioneta(Coche):
  def __init__(self, color, velocidad, cilindrada, carga):
    Coche.__init__(self, color, velocidad, cilindrada)
    self.carga = carga
  def __str__(self):
    return (" Color: {} Ruedas: {} Velocidad: {} Cilindrada: {} Carga: {}".format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga))

class Bicicleta(Vehiculo):
  def __init__(self, color, tipo):
    Vehiculo.__init__(self, color, 2)
    self.tipo = tipo
  def __str__(self):
    return (" Color: {} Ruedas: {} Tipo: {}".format(self.color, self.ruedas, self.tipo))

class Motocicleta(Bicicleta):
  def __init__(self, color, tipo, velocidad, cilindrada):
    Bicicleta.__init__(self, color, tipo)
    self.velocidad = velocidad
    self.cilindrada = cilindrada
  def __str__(self):
    return (" Color: {} Ruedas: {} Tipo: {} Velocidad: {} Cilindrada: {}".format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada))

chata1 = Camioneta("Rojo", 200, 2500, 1000)
moto1 = Motocicleta("Gris", "Urbana", 120, 200)
auto1 = Coche("Azul", 180, 1800)
bici1 = Bicicleta("Bordó", "Deportiva")

Vehiculo.catalogar(Vehiculo.vehiculos, 2)
'''

'''CASO 3
> Desarrollar un programa que cargue los datos de un triángulo.
> Implementar una clase con los métodos para inicializar los atributos, 
  imprimir el valor del lado con un tamaño mayor 
  y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulos():
  def __init__(self, ladoA, ladoB, ladoC):
    self.ladoA = ladoA
    self.ladoB = ladoB
    self.ladoC = ladoC

  def mayor(self):
    may = self.ladoA
    if self.ladoB > may:
      may = self.ladoB
    if self.ladoC > may:
      may = self.ladoC
    return may

  def tipo(self):
    tipo = "Escaleno"
    if (self.ladoA == self.ladoB == self.ladoC):
      tipo = "Equilátero"
    else:
      if (self.ladoA == self.ladoB) or (self.ladoB == self.ladoC) or (self.ladoA == self.ladoC):
        tipo = "Isósceles"
    return tipo

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))
Tri1 = Triangulos(lado1, lado2, lado3)
print(Tri1.mayor())
print(Tri1.tipo())
'''

'''CASO 4
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.
> Añadir contacto
> Lista de contactos
> Buscar contacto
> Editar contacto
> Cerrar agenda
'''
'''
class Agenda():
  def __init__(self, nombre, telefono, email):
    self.nombre = nombre
    self.telefono = telefono
    self.email = email

  def __str__(self):
    return ("Nombre: {} Teléfono: {} Email: {}".format(self.nombre, self.telefono, self.email))

  def esElBuscado(self, datoConocido, buscado):
    rta = False
    if (datoConocido == "N") and (buscado == self.nombre):
      rta = True
    if (datoConocido == "T") and (buscado == self.telefono):
      rta = True
    if (datoConocido == "E") and (buscado == self.email):
      rta = True
    return rta

  def editar(self, nombreNuevo, telefonoNuevo, emailNuevo):
    if nombreNuevo != "":
      self.nombre = nombreNuevo
    if telefonoNuevo != "":
      self.telefono = telefonoNuevo
    if emailNuevo != "":
      self.email = emailNuevo

def opcionElegida():
  Rta = ""
  while Rta == "":
    tecla = ord(getch())
    if tecla == 224:
      tecla2 = ord(getch())
      Rta = chr(tecla)+chr(tecla2)
    else:
      Rta = chr(tecla).upper()
  return Rta

def mostrarMenu(opciones):
  os.system ("cls")
  print("\n\n\t\t A  G  E  N  D  A\n")
  for o in opciones:
    print("\t\t", o)

import os
from msvcrt import getch
opciones = ["(A)ñadir contacto", "(L)ista de contactos", "(B)uscar contacto", "(E)ditar contacto", "(C)errar agenda"]
contacto = []

while True:
  mostrarMenu(opciones)
  opcion = opcionElegida()
  if (opcion == "A"):
    print("\n\t\t", opciones[0])
    nombre = input("\tNombre: ")
    telefono = input("\tTeléfono: ")
    email = input("\tEmail: ")
    contacto.append(Agenda(nombre, telefono, email))

  if (opcion == "L"):
    print("\n\t\t", opciones[1])
    for c in range(len(contacto)):
      print(c+1, contacto[c])
    pausa = opcionElegida()

  if (opcion == "B"):
    print("\n\t\t", opciones[2])
    print("\tSelecciona el dato conocido:")
    print("\t\tNombre")
    print("\t\tTeléfono")
    print("\t\tEmail")
    datoConocido = opcionElegida()
    if datoConocido == "N":
      buscado = input("Nombre buscado: ")
    if datoConocido == "T":
      buscado = input("Teléfono buscado: ")
    if datoConocido == "E":
      buscado = input("Email buscado: ")
    noEncontrado = True
    for c in range(len(contacto)):
      if contacto[c].esElBuscado(datoConocido, buscado):
        noEncontrado = False
        print("ENCONTRADO: ", end="")
        print(c+1, contacto[c])
    if noEncontrado:
      print("NO ENCONTRADO")
    pausa = opcionElegida()

  if (opcion == "E"):
    print("\n\t\t", opciones[3])
    reg = int(input("Ingrese el registro que desea editar: "))
    if (reg > 0 and reg <= len(contacto)):
      print("INGRESE EL DATO NUEVO O PULSE ENTER PARA DEJAR COMO ESTÁ")
      nombre = input("\tNombre: ")
      telefono = input("\tTeléfono: ")
      email = input("\tEmail: ")
      contacto[reg-1].editar(nombre, telefono, email)
    pausa = opcionElegida()

  if (opcion == "C"):
    break
'''
'''CASO 5
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: 
los tres atributos, sólo la hora y minuto,o sólo la hora. Crear además los métodos necesarios 
para modificar la hora en cualquier momento de forma manual. Mantenga la integridad de los datos 
en todo momento definiendo de tipo “private”. Crear una clase prueba_tiempo que prueba una 
hora concreta y la modifique a su gusto mostrándola por pantalla.
'''
'''
class Tiempo():
  def __init__(self, hora, minuto=0, segundo=0):
    self.hora = hora
    self.minuto = minuto
    self.segundo = segundo

  def __str__(self):
    return ("{}:{}:{}".format(dosDigitos(self.hora), dosDigitos(self.minuto), dosDigitos(self.segundo)))

  def set(self, hora, minuto, segundo):
    if hora is not None:
      self.hora = hora
    if minuto is not None:
      self.minuto = minuto
    if segundo is not None:
      self.segundo = segundo

  def subir(self, paraSubir):
    if (paraSubir == 0 and self.hora < 23):
      self.hora += 1
    if (paraSubir == 1 and self.minuto < 59):
      self.minuto += 1
    if (paraSubir == 2 and self.segundo < 59):
      self.segundo += 1

  def bajar(self, paraBajar):
    if (paraBajar == 0 and self.hora>0):
      self.hora -= 1
    if (paraBajar == 1 and self.minuto>0):
      self.minuto -= 1
    if (paraBajar == 2 and self.segundo>0):
      self.segundo -= 1

def opcionElegida():
  Rta = ""
  while Rta == "":
    tecla = ord(getch())
    if tecla == 224:
      tecla2 = ord(getch())
      Rta = chr(tecla)+chr(tecla2)
    else:
      Rta = chr(tecla).upper()
  return Rta

def dosDigitos(numero):
  n = str(numero)
  if len(n) == 1:
    rta = "0" + n
  else:
    rta = n
  return rta

import os
from msvcrt import getch
# h1 = Tiempo(10)
# print(h1)
# h2 = Tiempo(11, 20)
# print(h2)
# h3 = Tiempo(12, 30, 50)
# print(h3)
# h1.set(None, 55, None)
# print(h1)
# h1.set(None , None, 59)
# print(h1)

x = 0
h = Tiempo(10)
while True:
  os.system ("cls")
  print(h)
  for r in range(3):
    if r == x:
      print("── ", end="")
    else:
      print("   ", end="")
  print()

  Tecla = opcionElegida()
  if Tecla == chr(27):
    break
  if Tecla == chr(224)+chr(75): #IZQUIERDA
    x -= 1
    if x < 0: x = 2
  if Tecla == chr(224)+chr(77): #DERECHA
    x += 1
    if x > 2: x = 0
  if Tecla == chr(224)+chr(72): #ARRIBA
    h.subir(x)
  if Tecla == chr(224)+chr(80): #ABAJO
    h.bajar(x)
'''