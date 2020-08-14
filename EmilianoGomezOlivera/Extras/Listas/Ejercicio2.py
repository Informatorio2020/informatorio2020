#Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo
# estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

from os import system

materias = []

while(True):
    materias.append(input("Ingrese una materia: "))

    respuesta = input("¿Continuar? S/N: ")

    if(respuesta.lower() == "n"):
        break
    else:
        system("cls")

system("cls")

for actual in materias:
    print(f"Yo estudio {actual}")

input("\nFin")