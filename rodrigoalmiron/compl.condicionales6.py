print("BIENVENIDO AL SISTEMA DE SUELDOS DEL CLUB")
sueldo=int(input("Ingrese el sueldo del jugador"))
premio= int()
if sueldo <= 6000:
  	premio=sueldo+(sueldo*15)/100
  	print("su sueldo nuevo es:",premio)
elif sueldo>6000 and sueldo<=7900:
	premio=sueldo+(sueldo*10)/100
	print("su sueldo nuevo es:",premio)
elif sueldo>7900 and sueldo<=12000:
	premio= sueldo+(sueldo*6)/100
	print("su sueldo nuevo es:",premio)	  	
