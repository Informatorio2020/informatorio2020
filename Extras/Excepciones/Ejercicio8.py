#Ejercicio 8:
# Crear una función que reciba una lista y calcule la suma de todos los elementos,
# devolviendo None en caso de que alguno de ellos no pueda sumarse.

listaA = ["A", "E", "I", "O", "U"]
listaB = [1, 2, 3, 4, 5]
listaC = [1, 2, 3, 4 , "A"]

def sumarLista(lista, elemento):
    try:
        return sum(lista)
    except TypeError:
        return None

print(sumarLista(listaA, "I"))
print(sumarLista(listaB," 1"))
print(sumarLista(listaC," 1"))

input("\nFin")