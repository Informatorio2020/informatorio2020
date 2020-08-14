class Persona:

    def __init__(self,
                 DNI: int, Nombre: str, PrimerApellido: str,
                 SegundoApellido: str, TelefonoFijo: int, TelefonoMovil: int):
        self.__Max = 3
        self.__DNI = DNI
        self.__Nombre = Nombre
        self.__PrimerApellido = PrimerApellido
        self.__SegundoApellido = SegundoApellido
        self.__TelefonoFijo = TelefonoFijo
        self.__TelefonoMovil = TelefonoMovil
        self.__Prestamos = []

    def __GetPrestamos(self) -> int:
        return self.__Max

    def __GetDNI(self) -> int:
        return self.__DNI
    def __SetDNI(self, value: int) -> None:
        self.__DNI = value

    def __GetNombre(self) -> str:
        return self.__Nombre
    def __SetNombre(self, value: str) -> None:
        self.__Nombre = value

    def __GetPrimerApellido(self) -> str:
        return self.__PrimerApellido
    def __SetPrimerApellido(self, value: str) -> None:
        self.__PrimerApellido = value

    def __GetSegundoApellido(self) -> str:
        return self.__SegundoApellido
    def __SetSegundoApellido(self, value: str) -> None:
        self.__SegundoApellido = value

    def __GetTelefonoFijo(self) -> int:
        return self.__TelefonoFijo
    def __SetTelefonoFijo(self, value: int) -> None:
        self.__TelefonoFijo = value

    def __GetTelefonoMovil(self) -> int:
        return self.__TelefonoMovil
    def __SetTelefonoMovil(self, value: int) -> None:
        self.__TelefonoMovil = value

    def __Apellidos(self) -> str:
        return f"{self.__PrimerApellido} {self.__SegundoApellido}"

    def __NombreCompleto(self) -> str:
        return f"{self.__Nombre}, {self.__Apellidos()}"

    def __str__(self) -> str:
        return f"{self.__NombreCompleto()}. Prestamos disponibles: {self.__Max}"

    PrestamosRestantes = property(__GetPrestamos)
    DNI = property(__GetDNI, __SetDNI)
    Nombre = property(__GetNombre, __SetNombre)
    PrimerApellido = property(__GetPrimerApellido, __SetPrimerApellido)
    SegundoApellido = property(__GetSegundoApellido, __SetSegundoApellido)
    TelefonoFijo = property(__GetTelefonoFijo, __SetTelefonoFijo)
    TelefonoMovil = property(__GetTelefonoMovil, __SetTelefonoMovil)




class Prestamo:
    pass


x = Persona(0, "0", "0" ,"0", 0 ,0)

print(x.DNI)
x.DNI = 100
print(x.DNI)