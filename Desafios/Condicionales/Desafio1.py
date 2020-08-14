#DESAFÍO 1
# En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python 
# que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene 
# usando insecticida en su plantación. Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite 
# revisión de suelos en su plantación". Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos 
# ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".

tiempo = None

while(True):
    tiempo = input("¿Hace cuantos años utiliza insecticidas del tipo DDT?: ")

    try:
        tiempo = int(tiempo)

        if(tiempo < 0):
            print("Los años no pueden ser negativos")
        elif(tiempo > 10):
            print("Por favor solicite revisión de suelos en su plantación")
            break
        else:
            print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación")
            break
    except ValueError:
        print(f"No se pudo convertir '{tiempo}': No es un numero")

input("\nFin")