def funcion(nro):
	nro = nro+3
	print("Paso por valor", nro)

nro =23
funcion(nro)
print("---", nro)

def funcion2(lista):
	lista.append('nuevo')
	print('Paso por referencia',lista)


lista = [1,2, 'algo']
funcion2(lista)
print(lista)