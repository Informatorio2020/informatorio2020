#DESAFÍO 1
# Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
# a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al 
# usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 

from os import system

mockUser = "root"
mockPass = "admin"
intentos = 3

while(intentos != 0):
    userActual = input("Ingrese su usuario: ")
    system("cls")
    passActual = input("Ingrese su contraseña: ")
    system("cls")

    if(mockUser == userActual and mockPass == passActual):
        print(f"Bienvenido, {userActual}")
        break
    else:
        print("El usuario o la contraseña son incorrectos")
        intentos -= 1
        if(intentos == 0):
            print("La cuenta ha sido bloqueada")

input("\nFin")