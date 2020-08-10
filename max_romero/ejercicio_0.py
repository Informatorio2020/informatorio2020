"""CASO 4: Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones.

- Añadir contacto
- Lista de contactos
- Buscar contacto
- Editar contacto
- Cerrar agenda
"""

class Contacto: 
    def __init__(self, nombre, telefono, email):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email

