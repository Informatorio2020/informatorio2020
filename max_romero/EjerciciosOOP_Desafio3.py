""" Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos 
Imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es 
(equilátero, isósceles o escaleno)"""

class Triangulos:
    def __init__(self,lado1,lado2,lado3):
        self.lado1=int(input('Ingrese el lado 1: '))
        self.lado2=int(input('Ingrese el lado 2: '))
        self.lado3=int(input('Ingrese el lado 3: '))

 def lado_mayor(self,lado1,lado2,lado3):
    if self.lado1 > self.lado2 and self.lado1 > self.lado3:
        print("El lado mayor es: ",self.lado1)
    elif self.lado2 > self.lado3 and self.lado2 > self.lado1:
        print("El lado mayor es: ",self.lado2)
    else:
        print("El lado mayor es: ",self.lado3)
    
  def tipo_triang(self,lado1,lado2,lado3):
       if self.lado1 == self.lado2 and self.lado1 == self.lado3:
           print("Triangulo es equilatero")
       elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
         print("Triángulo es escaleno")
       else:
           print("Triángulo es isósceles")


#trianuglo1 = Triangulos(5,5,5)