#DESAFÍO 5
# La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio 
# y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
# La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y 
# los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
# Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se 
# encuentra.

barrio = None
centrico = None

while(True):
    barrio = input("Ingrese el nombre del barrio: ")

    respuesta = input("¿Es un barrio centrico? S/N (Por defecto No): ")
    centrico = False if (respuesta.lower() == "n") else True

    if((centrico and barrio[0].lower() < "m") or (centrico == False and barrio[0].lower() >= "m")):
        print(f"El barrio '{barrio}' corresponde a la seccion A")
        break
    else:
        print(f"El barrio '{barrio}' corresponde a la seccion B")
        break

input("\nFin")
