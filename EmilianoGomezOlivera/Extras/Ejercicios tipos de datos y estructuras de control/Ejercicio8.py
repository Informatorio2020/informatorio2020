#Ejercicio 8: 
# Escribí un programa para pedir al usuario su nombre y 
# luego el nombre de otra persona, almacenando cada 
# nombre en una variable. Luego mostrar en pantalla un 
# valor de verdad que indique si: los nombres de ambas 
# personas comienzan con la misma letra ó si terminan 
# con la misma letra. Por ejemplo, si los nombres 
# ingresados son María y Marcos, se mostrará True, ya 
# que ambos comienzan con la misma letra. Si los nombres 
# son Ricardo y Gonzalo se mostrará True, ya que ambos 
# terminan con la misma letra. Si los nombres son Florencia 
# y Lautaro se mostrará False, ya que no coinciden ni la 
# primera ni la última letra.

from os import system

nombreA = input("Ingrese el primer nombre: ")
system("cls")
nombreB = input("Ingrese el segundo nombre: ")
system("cls")

print(f"Primer nombre: {nombreA}\nSegundo nombre: {nombreB}")
if(nombreA[0].lower() == nombreB[0].lower()):
    print("Ambos nombres comienzan con la misma letra")
elif(nombreA[len(nombreA) - 1].lower() == nombreB[len(nombreB) - 1].lower()):
    print("Ambos nombres finalizan con la misma letra")
else:
    print("Los nombres no empiezan o terminan con la misma letra")

input("Fin")