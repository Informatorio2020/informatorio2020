#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
#el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.
#Añadir contacto
#Lista de contactos
#Buscar contacto
#Editar contacto
#Cerrar agenda

class Agenda():
    def __init__(self):
        self.contactos={}
        
    
    def menu(self):
        opcion=0
        while opcion !=5:
            print("Elige una opcion:")
            print("1-Añadir Contacto") 
            print("2-Listar Contacto") 
            print("3-Buscar Contacto")
            print("4-Editar Contacto") 
            print("5-Cerrar Agenda")
            opcion=int(input("Ingrese una opcion:"))
            if opcion==1:
                self.añadir()
            else:
                if opcion==2:
                    self.listar()
                else:
                    if opcion==3:
                        self.buscar()
                    else:
                        if opcion==4:
                            self.editar()
    
    def añadir(self):
        nombre=input("Ingrese el nombre del contacto:")
        tel=int(input("Ingrese el telefono:"))
        email=input("Ingrese el email:")
        self.contactos[nombre]=(tel,email)
        print("-------------------------------------")

    
    def listar(self):
        print("Listado de Agenda:")
        for nombre in self.contactos:
            print(nombre, "TEL:",self.contactos[nombre][0],"EMAIL:",self.contactos[nombre][1])
            print("---------------------------------------------------------")

    def buscar(self):
        nombre=input("Ingrese el nombre de la persona a buscar:")
        if nombre in self.contactos:
            print(nombre,"su telefono es",self.contactos[nombre][0], "su email es", self.contactos[nombre][1])
        else:
            print("el contacto no existe")
    
    def editar(self):
        nombre=input("Ingrese el nombre a modificar:")
        if nombre in self.contactos:
            nombre=input("El nombre es:")
            telefono=int(input("El telefono es:"))
            email=input("El email es:")
            self.contactos[nombre]=(telefono,email)
        else:
            print("No existe ese nombre:")


contacto1=Agenda()
contacto1.menu()



            
                  