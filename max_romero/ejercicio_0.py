"""
CASO 4: Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones.

- Añadir contacto[x]
- Lista de contactos[]
- Buscar contacto[]
- Editar contacto[]
- Cerrar agenda[]
"""

class Contact: 
    
    contact_list={}
    
    def __init__(self, name, phone_number, email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
    
    def __str__(self):
        return f'Nombre: {self.name}, Telefono: {self.phone_number}, E-mail: {self.email}.'
#Añadir contaco
    def add_contact(self):
        contact_list[self.nombre] = [self.phone_number, self,email]

#Getters y setters 

    def get_contact(self):
        return Contact
    
    def set_conctac(self, name, phone_number, email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        print('Se ha modificado el contacto')    


user_name=input('Ingrese nombre: ')
user_phone_number=input('Ingrese telefono: ')
user_email=input('Ingrese email: ')
