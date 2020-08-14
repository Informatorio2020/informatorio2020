#Desafío 2
# Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
# Tamaño Normal: Mensaje "Pez en buenas condiciones"
# Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
# Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
# Tamaño sobredimensionado: Mensaje "Pez contaminado"

while(True):
    print("¿Que peso tiene el pez?")
    print("1) Tamaño normal")
    print("2) Tamaño por debajo de lo normal")
    print("3) Tamaño por encima de lo normal")
    print("4) Tamaño sobredimensionado")

    opcion = input("\nElija una opcion: ")

    try:
        opcion = int(opcion)
        
        if(opcion == 1):
            print("Pez en buenas condiciones")
        elif(opcion == 2):
            print("Pez con problemas de nutricion")
        elif(opcion == 3):
            print("Tamaño por encima de lo normal")
        elif(opcion == 4):
            print("Pez contaminado")
        else:
            print("La opcion ingresada no es valida")            
        
        if(opcion >= 1 and opcion <= 4):
            break
        else:
            continue

    except ValueError:
        print(f"Error en la conversion de '{opcion}': No es un numero")

input("\nFin")