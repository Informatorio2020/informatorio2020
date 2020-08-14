# Ejercicio14
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras 
# y sustituya la primera por la segunda en la lista

import OperacionesComunes as Operacion

lista = []
palabraA = None
palabraB = None


while(True):
    lista.append(Operacion.solicitarCadena("Ingrese una palabra: ", palabras_minimas=1))

    if(Operacion.Si_No()):
        Operacion.limpiarPantalla()
        break
    else:
        Operacion.limpiarPantalla()        

while(True):
    if(palabraA == None):
        palabraA = Operacion.solicitarCadena("Escriba una de las palabras que ya ingreso: ", palabras_minimas=1)

        if(palabraA in lista):
            palabraA = lista.index(palabraA)            
        else:
            print(f"La palabra '{palabraA}' no esta en la lista")
            palabraA = None

    elif(palabraB == None):
        palabraB = Operacion.solicitarCadena("Escriba otra de las palabras que ya ingreso: ", palabras_minimas=1)

        if(palabraB in lista):
            palabraB = lista.index(palabraB)            
        else:
            print(f"La palabra '{palabraB}' no esta en la lista")
            palabraB = None
    
    else:
        break

Operacion.limpiarPantalla()

print(f"La lista original es: {lista}")

aux = lista[palabraA]
lista[palabraA] = lista[palabraB]
lista[palabraB] = aux

print(f"La lista cambiada es: {lista}")

input("\nFin")