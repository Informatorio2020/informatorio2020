#Ejercicio 3:
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
# has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
# cada una de las correspondientes notas introducidas por el usuario.

from os import system

materias = {}

while(True):
    materia = input("Ingrese una materia: ")

    nota = input("Ingrese la nota de la materia: ")

    try:
        nota = int(nota)        
        materias[materia] = nota

        respuesta = input("¿Continuar? S/N: ")        
        if(respuesta.lower() == "n"):
            break
        else:
            system("cls")
    except ValueError:
        print(f"No se puede convertir '{nota}': No es un numero")

system("cls")

for actual in materias:
    print(f"En {actual} has sacado {materias.get(actual)}")

input("\nFin")