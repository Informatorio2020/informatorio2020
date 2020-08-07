edades = (5,25,2,18,22,45,50,1,80,10)
cont= 0
for i in edades:
	if i > 20:
		cont +=1

print ( "Hay ", cont, "numeros mayores a 20")

vocales = ("a", "e", "i", "o", "u")

mostrar_post = vocales[2]

print ("en la posicion 2 se encuentra la letra: ", mostrar_post)

def saludo():
	print ("Hola Mundo")

saludo()

for letra in "Python":
	if letra == "h":
	continue
print("Letra actual: ", letra)