#Desafío 3
# Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados 
# en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas 
# ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
# Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.

from os import system

lista = []

class Ciudad:
    def __init__(self, nombre, arboles):
        self.nombre = nombre
        self.arboles = arboles

    def __str__(self):
        return (f"{self.nombre}: {self.arboles} arboles plantados")

def separar(lista):
    mejores = []
    resto = []

    for actual in lista:
        if(actual.arboles > 100):
            mejores.append(actual)
        else:
            resto.append(actual)

    mejores.sort(key=lambda x: x.arboles, reverse=True)
    resto.sort(key=lambda x: x.arboles, reverse=True)

    return (mejores, resto)

while(True):
    nombre = input("Ingrese el nombre de la ciudad: ")
    cantidad = input("¿Cuantos arboles ha plantado la ciudad?: ")

    if(cantidad.isnumeric()):
        cantidad = int(cantidad)

        if(cantidad >= 0):
            lista.append(Ciudad(nombre, cantidad))

            opcion = input("¿Desea seguir agregando ciudades? S/N (Por defecto Si): ")

            if(opcion.lower() == "n" or opcion.lower() == "no"):
                system("cls")
                break
            else:
                system("cls")
        else:
            system("cls")
            print("La cantidad de arboles plantados no puede ser negativa")
    else:
        system("cls")
        print(f"Error en la conversion de '{cantidad}': No es un numero")

nuevaLista, resto = separar(lista)

print("Las siguientes ciudades plantaron mas de 100 arboles: ")
for actual in nuevaLista:
    print(f"\t{actual}")

input("\nFin")