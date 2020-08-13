"""
CASO 4: Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones.

- Añadir contacto[]
- Lista de contactos[]
- Buscar contacto[]
- Editar contacto[]
- Cerrar agenda[]
"""


class Contact:
    
    def __init__(self, name, phone_number, email):
        self.name=name
        self.phone_number=phone_number
        self.email=email


class Agenda: 
    
    contact_list=[]

    def add_contact(self):
        input('Ingrese nombre: ')
        input('Ingrese telefono: ')
        input('Ingrese e-mail: ')
        contact_list.append()
        
        
        
            
    
    
    """def menu(self):
        opt=0
        while opt !=5:
            print("<<< MENU >>> ")
            print("1-Agregar contacto ") 
            print("2-Lista de contactos ") 
            print("3-Buscar contacto ")
            print("4-Editar contacto ") 
            print("5-Cerrar agenda ")
            
            opt=int(input("Ingrese una opcion:"))
            if opt==1:
                self.add_contact() 
            elif opt==2:
                #mostrar lista de contactos
            elif opt==3:
                #Buscar por nombre 
            elif opt==4:
                #Buscar y editar contacto
                print('<<< EDITAR CONTACTO >>>')
                print('1-Editar nombre')
                print('2-Editar numero de telefono')
                print('3-Editar e-mail')
                opt=int(input("Ingrese una opcion: "))
                if opt==1:
                    #Modificar nombre
                    def set_conctac_name(self, name):
                        self.name=input('Ingrese el nuevo nombre: ')
                        print('Se modifico el nombre del contacto')
                elif opt==2:
                    #Modificar telefono
                    def set_conctac_number(self, phone_number):
                        self.phone_number=input('Ingrese el nuevo telefono: ')
                        print('Se modificio el numero de telefono del contacto')
                elif opt==3:
                    #Modificar e-mail
                    def set_conctac_email(self, email):
                        self.email=input('Ingerse el nuevo e-mail: ')
                        print('Se modificio el e-mail del contaco')

            elif opt==5:
            #salir       
        
        
        
        
        
        else:
            if opcion==2:
                self.listar()
            else:
                if opcion==3:
                    self.buscar()
                else:
                    if opcion==4:
                        self.editar()"""