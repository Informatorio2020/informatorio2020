#Desafío 3	
# Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
# Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres 
# repetidos.

from os import system

agenda = {
    "biologo": [],
    "correo": []
}

while(True):
    nombre = input("Ingrese el nombre del biologo: ")
    correo = input("Ingrese el correo que utiliza: ")

    if(nombre in agenda.get("biologo")):
        system("cls")
        print("No se puede agregar por segunda vez al biologo en la misma agenda")
    else:
        agenda.get("biologo").append(nombre)
        agenda.get("correo").append(correo)

        opcion = input("\n¿Desea seguir agregando elementos? S/N (Por defecto Si)")

        if(opcion.lower() == "n" or opcion.lower() == "no"):
            system("cls")
            break
        else:
            system("cls")

print("Lista de contactos:\n")
for i in range(len(agenda.get("biologo"))):
    print(f"{agenda.get('biologo')[i]} ({agenda.get('correo')[i]})")

input("\nFin")