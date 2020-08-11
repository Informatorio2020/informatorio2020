class Contacto():
    def __init__(self, nombre, telefono, email):
        self.nombre= nombre
        self.telefono = telefono
        self.email = email
    
agenda = {}

nombre = input("Ingrese el nombre:")
telefono = input("Ingrese el teléfono:")
email = input("Ingrese el email:")

registro = Contacto(nombre, telefono, email)

def aniadir(datos):
 #   agregar = {"nombre":contacto.nombre, "telefono":contacto.telefono, "email":contacto.email}
    agenda[datos.nombre]=[datos.telefono, datos.email]
    print(agenda)
 #   agenda.append(agregar)

aniadir(registro)

