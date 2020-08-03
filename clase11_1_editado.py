#ESTRUCTURAS REPETITTIVAS

#while
control = 0
while control < 10:
	#codigo que se va a ejecutar
	control = control + 1
	print("---", control)

control = 0
while True:
	print("***", control)
	control += 1
	if control > 20:
		break


#For
for variable in range(1, 11):
	print("_*_", variable)


for caracter in "palabras":
	print("_*_", caracter)