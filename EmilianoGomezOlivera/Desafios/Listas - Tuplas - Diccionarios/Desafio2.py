#Desafío 2	
# Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y 
# niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el 
# numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición 
# sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero.

from os import system

factores = (
    "Las aguas residuales: \n\tProceden principalmente de los hogares, los comercios y la industria. Antes de ser vertidas al mar son tratadas para eliminar los mayores contaminantes, pero no suele ser suficiente para depurarlas por completo.\n",
    "Las sustancias químicas tóxicas: \n\tEs la principal causa de contaminación de los océanos. Las sustancias químicas provienen en su mayoría de las actividades industriales y afectan directamente a la salud de los seres marinos y terrestres.\n",
    "Las aguas pluviales: \n\tSon las utilizadas en las zonas de cultivo y por lo general suelen contener herbicidas, plaguicidas y fertilizantes que terminarán por filtrarse a las aguas subterráneas y a los ríos para finalmente terminar en el mar.\n",
    "El vertido de plásticos: \n\tLos plásticos pueden llegar a tardar en degradarse entre los 150 y los 1000 años. Todos los residuos de plásticos vertidos al mar afectan directamente a la fauna marina, ya que confunden estos desechos con comida o se quedan atrapados.\n",
    "Los vertidos de petróleo: \n\tPor norma general estos vertidos suelen ser accidentes, pero esto no resta el daño que provoca a los seres vivos de la zona.\n",
    "La actividad minera en alta mar: \n\tProvoca contaminación acústica en el mar perjudicando a las especies más sensibles a las ondas acústicas, ya que pueden llegar a confundirlas y desorientarse.\n",
    "El cambio climático: \n\tNo es un factor contaminante directamente, pero si influye en el océano. El aumento de las temperaturas provoca el descongelamiento de los polos, el aumento del nivel del mar y de su temperatura, modifica las rutas migratorias de las especies y puede llegar a acidificarlo.\n"
)

while(True):
    opcion = input("Los mares y oceanos del mundo se ven afectados por 7 factores que dañan el ecosistema.\nElegi un numero del 1 al 7 para ver esos factores, presiona 0 para salir: ")

    if(opcion.isnumeric()):
        opcion = int(opcion)

        if(opcion == 0):
            break
        elif(opcion < 1 or opcion > 7):
            system("cls")
            print("Tenes que elegir una numero del 1 al 7.")
        else:
            system("cls")
            print(factores[opcion - 1])
    else:
        system("cls")
        print("Tenes que elegir un numero del 1 al 7")

input("\nFin")