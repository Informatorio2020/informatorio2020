class Contacto():

    agenda = []

    def __init__(self, nombre, telefono, email):
        self.nombre= nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return "Nombre: {} - Teléfono: {} - Email: {}".format(self.nombre,self.telefono,self.email)

    def aniadir(self):
        Contacto.agenda.append(self)#[self.nombre] = [self.telefono,self.email]

    def listar(self):
        for a in Contacto.agenda:
            print(a)

    def buscar(self, nombre):
        for a in Contacto.agenda:
            if a.nombre == nombre:
                print(a)

    def editar(self, editar):
        for a in Contacto.agenda:
            if a.nombre == editar:            
                a.nombre = input("Ingrese el nombre:")
                a.telefono = input("Ingrese el teléfono:")
                a.email = input("Ingrese el email:")
                return("Contacto editado")
        return("No se encuentra el contacto")

print("-----------------------------------------")
print("          Agenda de contactos            ")
print("-----------------------------------------")
salir=1
while salir != 0:
    print("1- Añadir contacto       2- Lista de contactos")
    print("3- Buscar contacto       4- Editar contacto")
    print("0- Salir")
    salir = int(input("Ingrese una opción: "))

    if salir == 1:
        nombre = input("Ingrese el nombre:")
        telefono = input("Ingrese el teléfono:")
        email = input("Ingrese el email:")

        registro = Contacto(nombre, telefono, email)
        registro.aniadir()
    
    elif salir == 2:
        Contacto.listar(Contacto.agenda)

    elif salir == 3:
        buscado = input("Ingrese un nombre a buscar: ")
        Contacto.buscar(Contacto.agenda,buscado)
    elif salir == 4:
        editar = input("Ingrese el nombre de un contacto a editar: ")
        print(Contacto.editar(Contacto.agenda,editar))
        
        #Esto lo agregue para dar conflictos
        #Soy perversita
