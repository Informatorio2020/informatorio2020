#Ejercicio 3:
# Escribí un programa que solicite al usuario el ingreso de 
# dos palabras, las cuales se guardarán en dos variables 
# distintas. A continuación, almacená en una variable la 
# concatenación de la primera palabra, más un espacio, más 
# la segunda palabra. Mostrá este resultado en pantalla. 

from os import system

# Se solicitan los datos sin ningun control ya que se requieren unicamente cadenas de caracteres
primeraPalabra = input("Ingrese la primera palabra: ")
system("cls")
segundaPalabra = input("Ingrese la segunda palabra: ")
system("cls")
concatenacion = primeraPalabra + " " + segundaPalabra

print(concatenacion)

input("\nFin")