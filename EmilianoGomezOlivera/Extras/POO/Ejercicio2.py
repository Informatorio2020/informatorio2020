#Ejercicio 2:
# Crea una clase Fecha. La clase contendrá además del constructor, métodos set y get y el
# método __str__(), un método para comprobar si la fecha es correcta y otro para modificar la
# fecha actual por otra.


class Fecha:

    def __init__(self, anho: int, mes: int, dia: int):
        self.__Anho = anho
        self.__Mes = mes
        self.__Dia = dia

    def comprobar(self):
        mesesLargos = (1, 3, 5, 7, 8, 10, 12)
        no = "La fecha es incorrecta"
        si = "La fecha es correcta"

        if self.__Mes == 2:
            if self.__Anho % 4 == 0:
                if self.__Dia <= 29:
                    print(si)
                else:
                    print(no)
            else:
                if self.__Dia <= 28:
                    print(si)
                else:
                    print(no)
        elif self.__Mes in mesesLargos:
            if self.__Dia <= 31:
                print(si)
            else:
                print(no)
        elif not(self.__Mes in mesesLargos) and 11 >= self.__Mes > 0:
            if self.__Dia <= 30:
                print(si)
            else:
                print(no)
        else:
            print(no)

    def modificar(self, anho: int = 0, mes: int = 0, dia: int = 0):
        if anho != 0:
            self.__Anho = anho

        if mes != 0:
            self.__Mes = mes

        if dia != 0:
            self.__Dia = dia

    def __str__(self):
        return f"{self.__Dia}/{self.__Mes}/{self.__Anho}"


x = Fecha(2012, -12, 29)
x.comprobar()
x.modificar(2017, 11, 21)
print(x)
x.comprobar()