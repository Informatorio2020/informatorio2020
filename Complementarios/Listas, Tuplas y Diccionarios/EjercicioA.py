# Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo

from os import system

palabra = []
conjunto = ""
palindromo = True
inverso = None

while(True):
    letra = input("Ingrese una letra: ")

    if(letra == "" or letra == " " or len(letra) > 1):
        system("cls")
        print("Solo ingrese una letra")
    else:
        palabra.append(letra)
        conjunto += letra

        opcion = input("Ingrese # para salir (Cualquier otra letra continuara con el programa): ")

        system("cls")
        if(opcion == "#"):
            break
            

inverso = palabra[::-1]

for x in range(len(palabra)):
    if(palabra[x].lower() != inverso[x].lower()):
        palindromo = False
        break

print(f"La palabra '{conjunto} ' {'es un palindromo' if (palindromo) else 'no es un palindromo'}")

input("\nFin")