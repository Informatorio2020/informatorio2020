#Ejercicio 9:
# Diseñar una función que recibe una lista y un índice, y devuelve el elemento que ocupa
# dicha posición o None si el indice esta fuera de los limites de la lista.

lista = ["A", "E", "I", "O", "U"]

def buscar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None

print(buscar(lista, 6))
print(buscar(lista, 2))

input("\nFin")