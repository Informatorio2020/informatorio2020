#Desafío 2
# Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se 
# cumpla lo siguiente:
#     Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
#     Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
#     Si ambos números son iguales, debe devolver el nombre de ambas.

def reciclado(cantidadA, cantidadB):
    ciudadA = "Alfa"
    ciudadB = "Omega"

    if(cantidadA > cantidadB):
        print(f"\nLa ciudad {ciudadA} reciclo mas")
    elif(cantidadB > cantidadA):
        print(f"\nLa ciudad {ciudadB} reciclo mas")
    else:
        print(f"\nLa ciudad {ciudadA} y la ciudad {ciudadB} reciclaron lo mismo")

pesoA = int(input("Ingrese las toneladas recicladas por la primera ciudad: "))
pesoB = int(input("Ingrese las toneladas recicladas por la segunda ciudad: "))

reciclado(pesoA, pesoB)

input("\nFin")