tipodepizza = input("Ingrese 1, si desea una pizza vegetariana. En caso de querer una pizza no vegetariana ingrese 2:\n")

if tipodepizza == "1":
	
	ingredientes_veg = input("Ingredientes disponibles: Pimiento y Rucula. Escoja solo uno: \n ")
	
	if ingredientes_veg == "pimiento":

		print("La pizza que ordenó es vegetariana. Sus ingredientes son: Tomate, Muzzarella, Pimiento.")

	else:
			
		print("La pizza que ordenó es vegetariana. Sus ingredientes son: Tomate, Muzzarella, Rúcula.")

else:

	ingredientes_noveg = input("Ingredientes disponibles: Jamón y Panceta. Escoja solo uno: \n")
		
		
	if ingredientes_noveg == "jamon":
		
		print("La pizza que ordenó es no vegetariana. Sus ingredientes son: Tomate, Muzzarella, Jamón.")
		
	else:
		
		print("La pizza que ordenó es no vegetariana. Sus ingredientes son: Tomate, Muzzarella, Panceta.")