'''CASO 4
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.
> Añadir contacto
> Lista de contactos
> Buscar contacto
> Editar contacto
> Cerrar agenda
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

