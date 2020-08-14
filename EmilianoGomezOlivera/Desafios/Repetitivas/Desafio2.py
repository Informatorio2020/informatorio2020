#DESAFÍO 2
# Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
# Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de 
# personas. Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos 
# de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

from os import system

class Contador:
    total = 0
    menosDeCien = 0
    menosDeDoscientos = 0
    masDeDoscientos = 0

    def contar(self, dato):
        try:
            aux = int(dato)

            if(aux > 0):
                if(aux < 100):
                    self.menosDeCien += 1
                elif(aux >= 100 and aux < 200):
                    self.menosDeDoscientos += 1
                else:
                    self.masDeDoscientos += 1
                self.total += 1                
        except ValueError:
            print(f"Error en la conversion de '{dato}': No es un numero")
    
    def informar(self):
        print(f"Menos de 100 colillas recolectadas: {self.menosDeCien} ({round(self.menosDeCien / self.total, 2)}%)")
        print(f"Mas de 100 colillas y menos de 200 colillas recolectadas: {self.menosDeDoscientos} ({round(self.menosDeDoscientos / self.total, 2)}%)")
        print(f"Mas de 200 colillas recolectadas: {self.masDeDoscientos} ({round(self.masDeDoscientos / self.total, 2)}%)")

miContador = Contador()

while(True):
    system("cls")
    miContador.contar(input("¿Cuantas colillas recolecto?: "))
    opcion = input("¿Continuar? S/N (Por defecto No)")

    if(opcion.lower() == "s"):
        continue
    else:
        break

miContador.informar()

input("\nFin")