listamaterias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
materias = []
for elemento in listamaterias:
    nota = float(input("¿Qué nota has sacado en " + elemento + "?"))
    if nota >= 6:
        materias.append(elemento)
for elemento in materias:
    listamaterias.remove(elemento)
print("Tienes que repetir " + str(listamaterias))


