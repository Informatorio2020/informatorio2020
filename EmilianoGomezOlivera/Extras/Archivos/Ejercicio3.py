from os import system, path
from io import open
import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return (f"{self.nombre}\t{self.vida}\t{self.ataque}\t{self.defensa}\t{self.alcance}")

class Gestor:
    personajes = []

    def __init__(self):
        system("cls")
        print("Iniciando gestor de personajes")
        if(path.isfile("personajes.pckl")):
            print("Cargando datos guardados")
            if (path.getsize("personajes.pckl") > 0):      
                archivo = open("personajes.pckl", "rb")
                self.personajes = pickle.load(archivo)
                archivo.close()
            else:
                self.personajes = []
        else:
            print("Creando archivo de guardado")
            open("personajes.pckl", "xb")

        input("Finalizada las preoperaciones. Presion Enter para continuar.")

    def menu(self):
        system("cls")
        while(True):            
            print("-----------------------------------------------")
            print("1. Crear personaje")
            print("2. Borrar personaje")
            print("3. Mostrar personajes")
            print("4. Salir")
            print("-----------------------------------------------")
            operacion = input("Ingrese la operacion a realizar: ")

            if(operacion.isnumeric()):
                operacion = int(operacion)

                if(operacion == 1):
                    self.crear()
                    system("cls")
                elif(operacion == 2):
                    self.borrar()
                    system("cls")
                elif(operacion == 3):
                    self.mostrar()
                    system("cls")
                elif(operacion == 4):
                    system("cls")
                    print("Se ha finalizado el programa")
                    input("Presione Enter para cerrar el programa")
                    break
                else:
                    system("cls")
                    print("Operacion no valida")
            else:
                system("cls")
                print("Operacion no valida")
    
    def crear(self):
        existe = False
        system("cls")
        nombre = input("Ingrese el nombre del personaje: ")
        vida = input("Ingrese la vida del personaje: ")
        ataque = input("Ingrese el ataque del personaje: ")
        defensa = input("Ingrese la defensa del personaje: ")
        alcance = input("Ingrese el alcance del personaje: ")

        for actual in self.personajes:
            if(actual.nombre.lower() == nombre.lower()):
                existe = True
                break

        if(existe):
            system("cls")
            print(f"No se puede crear al personaje '{nombre}' porque ya existe.")
            input("Presione Enter regresar al menu")
        else:
            self.personajes.append(Personaje(nombre, vida, ataque, defensa, alcance))

            archivo = open("personajes.pckl", "wb")
            pickle.dump(self.personajes, archivo)
            archivo.close()

            print("\nPersonaje creado con exito")
            input("Presione Enter regresar al menu")
    
    def borrar(self):
        system("cls")
        while(True):            
            i = 0

            print("Escriba @ para salir")
            print(f"Indice\tNombre\t\tVida\tAtaque\tDefensa\tAlcance")
            for actual in self.personajes:
                print(f"{i}\t{actual}")
                i += 1

            seleccion = input("\nIngrese el indice del personaje que quiere borrar: ")

            if(seleccion.isnumeric()):
                seleccion = int(seleccion)

                if(seleccion < 0 or seleccion >= len(self.personajes)):
                    system("cls")
                    print("Valor no valido, ingrese un nuevo valor dentro del rango")
                else:
                    system("cls")
                    del self.personajes[seleccion]
                    archivo = open("personajes.pckl", "wb")
                    pickle.dump(self.personajes, archivo)
                    archivo.close()
            elif(seleccion == "@"):
                break
            else:
                system("cls")
                print(f"'{seleccion}' no es un valor valido")
    
    def mostrar(self):
        system("cls")
        print(f"Nombre\t\tVida\tAtaque\tDefensa\tAlcance")
        for actual in self.personajes:
            print(actual)
        
        input("\nPresione Enter para regresar al menu")

miGestor = Gestor()

miGestor.menu()
