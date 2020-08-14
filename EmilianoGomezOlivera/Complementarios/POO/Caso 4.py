from os import system

class Contacto:

    def __init__(self, nombre: str = None, telefono: str = None, email: str = None):
        """
        Constructor de la clase

        :param nombre: Por defecto None. Nombre del contacto.
        :param telefono: Por defecto None. Telefono del contacto.
        :param email: Por defecto None. Email del contacto.
        """
        self.__Nombre = nombre
        self.__Telefono = telefono
        self.__Email = email

    def nombre(self, valor: str = None):
        """
        Funcion que permite cambiar el nombre del contacto si se le pasa un valor. Si no se le passa nada
        devuelve el valor que tiene el atribute en el momento dado.

        :param valor: Si se le pasa un valor reemplazara el valor que contiene el atributo Nombre por el nuevo valor,
        siempre retorna el valor actual del atributo Nombre.
        :return: self.Nombre
        """
        if not(valor == None):
            self.__Nombre = valor

        return self.__Nombre

    def telefono(self, valor: str = None):
        """
        Funcion que permite cambiar el telefono del contacto si se le pasa un valor. Si no se le passa nada
        devuelve el valor que tiene el atribute en el momento dado.

        :param valor: Si se le pasa un valor reemplazara el valor que contiene el atributo Telefono por el nuevo valor,
        siempre retorna el valor actual del atributo Telefono.
        :return: self.telefono
        """
        if not(valor == None):
            self.__Telefono = valor

        return self.__Telefono

    def email(self, valor: str = None):
        """
        Funcion que permite cambiar el email del contacto si se le pasa un valor. Si no se le passa nada
        devuelve el valor que tiene el atribute en el momento dado.

        :param valor: Si se le pasa un valor reemplazara el valor que contiene el atributo Email por el nuevo valor,
        siempre retorna el valor actual del atributo Email.
        :return: self.Nombre
        """
        if not(valor == None):
            self.__Email = valor

        return self.__Email

    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return self.__Nombre == other.nombre() and self.__Telefono == other.telefono() and self.__Email == other.email()
        else:
            return False

    def __str__(self):
        return f"Nombre: {self.__Nombre}\nTelefono: {self.__Telefono}\nEmail: {self.__Email}"

class Agenda:

    def __init__(self):
        self.__Lista = []
        self.__Estado = True

    def agregar(self, nuevoContacto: Contacto):
        """
        Agrega un nuevo contacto a la lista

        :param nuevoContacto: Objeto que se desea agregar
        :return: None
        """
        self.__Lista.append(nuevoContacto)

    def borrar(self, elemento: Contacto):
        """
        Elimina un contacto en base a una instancia similar, devuelve un booleano que determina el exito de la operacion

        :param elemento: Elemento similar al que se busca borrar
        :return: bool
        """
        try:
            posicion = self.__Lista.index(elemento)
            del self.__Lista[posicion]
            return True
        except ValueError:
            print("No se ha encontado el elemento ha borrar")
            return False

    def buscar(self, nombre: str):
        """
        Devuelve un contacto en base al nombre del mismo

        :param nombre: Nombre del contacto que se buscara
        :return: Contacto (Por defecto None)
        """
        respuesta = None

        for actual in self.__Lista:
            if actual.nombre() == nombre:
                respuesta = actual
                break

        return respuesta

    def editar(self, nombre: str):
        resultado = self.buscar(nombre)

        if resultado == None:
            return False
        else:
            resultado.nombre(input("Ingrese el nuevo nombre: "))
            resultado.telefono(input("Ingrese el nuevo telefono: "))
            resultado.email(input("Ingrese el nuevo email: "))
            return True

    def listar(self):
        for actual in self.__Lista:
            print(f"{actual}\n")

    def estado(self):
        """
        Devuelve si la agenda esta abierta o cerrada.

        :return: self.Estado
        """
        return self.__Estado

def menu():
    miAgenda = Agenda()

    texto = """    1. Añadir contacto
    2. Listar contactos
    3. Buscar contacto
    4. Editar contacto
    5. Salir"""
    while(True):
        print(texto)
        opcion = input("Ingrese una opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)

            system("cls")
            if opcion == 1:
                nuevoContacto = Contacto(
                    input("Ingrese el nombre del contacto: "),
                    input("Ingrese el telefono del ontacto: "),
                    input("Ingrese el email del contacto: ")
                )

                miAgenda.agregar(nuevoContacto)
                system("cls")

            elif opcion == 2:
                miAgenda.listar()
                input("\nPresion Enter para continuar")
                system("cls")

            elif opcion == 3:
                resultado = miAgenda.buscar(input("Ingrese el nombre del contacto ha buscar: "))

                if resultado == None:
                    print("No se ha encontrado ningun contacto con ese nombre")
                else:
                    print("Resultado: ")
                    print(resultado)
                    input("\nPresione Enter para continuar")
                    system("cls")

            elif opcion == 4:
                miAgenda.editar(input("Ingrese el nombre del contacto ha buscar para editar: "))

            elif opcion == 5:
                break

            else:
                system("cls")
                print("La opcion es ingresada no es valida")

menu()

input("\nFin")