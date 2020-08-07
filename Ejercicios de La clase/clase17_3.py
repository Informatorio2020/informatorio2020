#diccionarios

diccionario = {}
diccionario = {"clave": "valor", "otra": "otro valor"}

diccionario["clave2"] = "valor2"

if "clave" not in diccionario.keys():
	diccionario.update({"clave": "valor234"})

for i in diccionario:
	print(i, diccionario[i])

print(diccionario.keys())



diccionario.get("clav34", "No existe")