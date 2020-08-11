"""
CASO 4: Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones.

- Añadir contacto[o]
- Lista de contactos[]
- Buscar contacto[x]
- Editar contacto[x]
- Cerrar agenda[]
"""

class Contact: 
    
    contact_list={}
    
    """def menu(self):
    opt=0
    while opt !=5:
        print("<<< MENU >>>: ")
        print("1-Agregar contacto ") 
        print("2-Lista de contactos ") 
        print("3-Buscar contacto ")
        print("4-Editar contacto ") 
        print("5-Cerrar agenda ")
        
        opt=int(input("Ingrese una opcion:"))
        if opt==1:
            self.añadir() 
        else:
            if opcion==2:
                self.listar()
            else:
                if opcion==3:
                    self.buscar()
                else:
                    if opcion==4:
                        self.editar()"""

    def __init__(self, name, phone_number, email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
    
    def __str__(self):
        return f'Nombre: {self.name}, Telefono: {self.phone_number}, E-mail: {self.email}.'
#Añadir contaco
    #def add_contact(self):
        #contact_list[self.nombre] = [self.phone_number, self,email]

#Getters

    def get_contact_name(self):
        return f'Nombre: {self.name}'
   
    def get_contact_phone(self):
        return f'Telefono: {self.phone_number}'

    def get_contact_(self):
        return f'E-mail: {self.email}'

#Setters

    def set_conctac_name(self, name):
        self.name=name
        #print('Se ha modificado el nombre contacto')

    def set_conctac_number(self, phone_number):
        self.phone_number=phone_number
        #print('Se ha modificado el numero de telefono del contacto') 

    def set_conctac_email(self, email):
        self.email=email
        #print('Se ha modificado el email del contacto')     


"""user_name=input('Ingrese nombre: ')
user_phone_number=input('Ingrese telefono: ')
user_email=input('Ingrese email: ')"""

concatc1 = Contact('Max','3624556655','max.r@mail.com')
print(concatc1.name)
concatc1.set_conctac_name('Mara')
print(concatc1.name)
concatc1.set_conctac_number('0303456')
print(concatc1.phone_number)
concatc1.set_conctac_email('correo@correito.com')
print(concatc1.email)
