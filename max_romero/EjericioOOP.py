"""Definir una clase Persona los atributos nombre y dni. 
Definir otra clase llamada Paciente con el atributo historia_clinica
que herede de la clase Persona. Para ambas clases crear el constructor 
"""

class Persona:
    def __init__(self, nombre, dni):
        self.nombre=nombre
        self.dni=dni

class Paciente(Persona):
    def __init__(self,nombre, dni, historia_clinica):
        super.__init__(dni,nombre, dni)
        self.historia_clinica=historia_clinica
