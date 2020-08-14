#Desafío 3
# Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el 
# suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir 
# vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización 
# de fertilizantes.

cantidad = None
matorral = None

while(True):
    cantidad = input("Ingrese el % de compuesto presente en el suelo: ")

    try:
        cantidad = float(cantidad)

        if(cantidad >= 0 and cantidad <= 100):
            respuesta = input("¿Existen matorrales en la vegetacion? S/N (Por defecto Si): ")
            matorral = True if (respuesta.lower() != "n") else False

            if(matorral):
                print("No es factible el uso de fertilizantes")
                break
            else:
                if(cantidad >= 10):
                    print("Es factible el uso de fertilizantes")
                    break
                else:
                    print("No es factible el uso de fertilizantes")
                    break
        else:
            print("El compuesto en suelo no puede ser mayor al 100% ni menor al 0%")
    except ValueError:
        print(f"Error en la conversion de {cantidad}: No es un numero")

input("\nFin")