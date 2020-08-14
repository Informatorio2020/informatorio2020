#Ejercicio 7:
# Desarrollar una función que recibe una lista y el elemento a buscar, devolviendo su posición
# si existe y -1 en caso de que no

lista = ["A", "E", "I", "O", "U"]

def buscar(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1

print(buscar(lista, "I"))
print(buscar(lista," 1"))

input("\nFin")