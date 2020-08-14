#Ejercicio 1
# ECrear un script llamado personas.py que lea los datos de un fichero de texto, que transforme cada fila en 
# un diccionario y lo añada a una lista llamada personas. Luego recorre las personas de la lista y para cada 
# una muestra de forma amigable todos sus campos.
# El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo 
# previamente):
#       1;Carlos;Pérez;05/01/1989
#       2;Manuel;Heredia;26/12/1973
#       3;Rosa;Campos;12/06/1961
#       4;David;García;25/07/2006
# Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.

personas = []

fichero = open('Datos1.txt', encoding="utf8")
texto = fichero.readlines()
fichero.close()

for actual in texto:
    aux = actual.split(";")
    diccionario = {
        "id" : aux[0],
        "nombre" : aux[1],
        "apellido" : aux[2],
        "nacimiento" : aux[3].replace("\n", "")
    }
    personas.append(diccionario)

for actual in personas:
    print(actual)


input("\nFin")