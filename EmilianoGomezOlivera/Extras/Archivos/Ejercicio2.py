#Ejercicio 2
# Crear un script llamado contador.py que realice varias tareas sobre un fichero
# llamado contador.txt que almacenará un contador de visitas (será un número):
#       ● Nuestro script trabajará sobre el fichero contador.txt . Si el fichero no
#           existe o está vacío lo crearemos con el número 0. Si existe simplemente
#           leeremos el valor del contador.
#       ● Luego a partir de un argumento:
#           ● Si se envía el argumento inc, se incrementará el contador en
#               uno y se mostrará por pantalla.
#           ● Si se envía el argumento dec , se decrementará el contador en
#               uno y se mostrará por pantalla.
#           ● Si no se envía ningún argumento (o algo que no sea inc o dec),
#               se mostrará el valor del contador por pantalla.
#       ● Finalmente guardará de nuevo el valor del contador de nuevo en el
#           fichero.
#       ● Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje:
#           Error: Fichero corrupto.

from os import system, path
from io import open

class Contador:
    valor = 0

    def __init__(self):
        if(not(path.isfile("contador.txt"))):
            archivo = open("contador.txt", "wt")
            archivo.write(str(self.valor))
            archivo.close()
        else:
            archivo = open("contador.txt", "rt")
            self.valor = int(archivo.read())
            archivo.close()

    def modificar(self, operacion = "inc"):
        system("cls")
        
        if(operacion.lower() == "inc" or operacion.lower() == "dec"):
            archivo = open("contador.txt", "wt")

            if(operacion.lower() == "inc"):            
                self.valor += 1
                archivo.write(str(self.valor))
                print(f"Contador: {self.valor}")
            elif(operacion.lower() == "dec"):
                self.valor -= 1
                archivo.write(str(self.valor)) 
                print(f"Contador: {self.valor}")

            archivo.close()
        else:
            print(f"Contador: {self.valor}")
        
        

    def __str__(self):
        return self.valor
            
miContador = Contador()

while(True):
    tarea = input(f"Operaciones posibles:\n\t'inc' (Incrementar)\n\t'dec' (Decrementar)\n\t'ver' (Mostrar contador, operacion por defecto)\n\t0 (Finalizar programa)\nRealizar: ")

    if(tarea == "0"):
        break
    else:
        miContador.modificar(tarea)

input("\nFin")