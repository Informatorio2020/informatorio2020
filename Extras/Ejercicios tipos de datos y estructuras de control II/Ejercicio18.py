#Ejercicio 18:
# Escribí un programa que pregunte al usuario si desea analizar calificaciones de alumnos y,
# sólo si responde “S” comenzará el procesamiento de los datos, hasta que el usuario ingrese
# algo diferente de “S”. Por cada alumno, permitir ingresar su calificación. Si es mayor a 4 el
# alumno está aprobado. Finalmente, mostrar “Porcentaje de alumnos aprobados: x %”
# (donde x es el porcentaje de aprobados sobre el total de calificaciones procesadas).
# También se debe imprimir “Promedio de los aprobados: y” (donde y es la calificación
# promedio, sólo de los alumnos aprobados).

from os import system

promedioNotaAprobados = 0
aprobados = 0
total = 0

while(True):
    opcion = input("¿Analizar calificaciones? S/N: ")

    if(opcion.lower() != "s"):
        break
    else:
        system("cls")
        nota = input("Ingrese la nota: ")

        try:
            nota = int(nota)

            if(nota >= 4):
                aprobados += 1
                promedioNotaAprobados += nota

            total += 1
        except ValueError:
            print(f"Error en la converison de {nota}: No es un numero")       

system("cls")

print(f"Calificaciones totales: {total}")
print(f"Nº de aprobados: {aprobados}")
print(f"% de aprobados: {round(((aprobados / total) * 100), 2)}")
print(f"Promedio de nota: {round((promedioNotaAprobados / total), 2)}")

input("\nFin")