#MANEJO DE ERRORES
#EXCEPCIONES

#Podemos manejar los errores de forma generica
def multiplicar(valor):
	try:
		print(10/valor)

	except:
		print("No se puede hacer la operacion")

multiplicar(3)
multiplicar("hola")
multiplicar(0)



#Podemos manejar distintos tipos de errores de maneras diferentes
def division(num):
	try:
		print(10/num)

	#Error de tipo 
	except TypeError:
		print("No se puede dividir por ese valor")

	#Error de division por 0
	except ZeroDivisionError:
		print("No puedo hacer divisiones por cero")


division(3)
division("hola")
division(0)


#Podemos manejar distintos tipos de errores
def desapilar():
	try:
		lista.pop()

	#Error de indice, en este caso para una lista vacia
	except IndexError:
		print("Tu lista ya esta vacia")


lista= []
desapilar()




#Podemos ejecutar codigo alternativo
def recuperar_primer_elemento():
	try:
		print(lista[0])

	#Error de indice, en este caso para una lista vacia
	except TypeError:
		print(None)
	except Exception:
		print("Otro tipo de errores")


recuperar_primer_elemento()



def multiplicar(valor):
	try:
		print(10*int(valor))

	except ValueError:
		print("No se puede convertir a entero")



multiplicar("hola")



#Podes tratar diferentes errores al mismo tiempo
def divisiones(valor):
	try:
		print(10/int(valor))

	except (ValueError, ZeroDivisionError, IndexError):
		print("Verifique la informacion que esta proporcionando")

divisiones("hola")
divisiones(0)

#Podemos usarlo dentro de un ciclo
while True:
	try:
		n = float(input("Introduce un número: "))        
		m = 4
		print("Ya almacene los valores")
		print("{}/{} = {}".format(n,m,m/n))
		# Si todo ha salido bien finaliza la iteracion
		break
	except:        
		print("Ha ocurrido un error, introduce bien el número")




#podemos usarlo por fuera de una estructura en el programa principal
print("Este programa trata errores")
try:
	valor = lista
except NameError:
	print("La variable no fue definida")


#Else
#Finally
def calculo_masa_corporal(diccionario):
	try:
		#El caso de que el diccionario traiga los valores del peso y la altura
		peso= diccionario["peso"]
		altura= diccionario["altura"]
		print("Estoy en el try")
	except KeyError:
		#El diccionario ya trae el calculo del indice de masa corporal
		indice = diccionario["indice"]
		print("Estoy en el except")
	else:
		#Si ejecuto lo que se encuntra del tro del try de forma exitosa, ingresara a el else
		#Donde realizara el calculo
		indice = peso / altura
		print("Estoy en el else")
	finally:
		#Se ejecuta siempre ocurra o no un error
		print(indice)

calculo_masa_corporal({"peso": 70, "altura": 1.80})
calculo_masa_corporal({"indice": 21.6})
calculo_masa_corporal({"peso": 70, "indice": 21.6})



#podemos lanzar las excepciones de forma manual

lista=[]
try:
	if len(lista) == 0:
		raise NameError("Longitud O no me deberia dar un error en este caso pero yo lo lanzo manualmente por que asi me parece")
except NameError as e:
	print("la lista no tiene elementos")
	print("nombre del error", type(e).__name__)
	print("Descripcion del error", e)
