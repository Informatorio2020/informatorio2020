class Serie():
    def __init__(self,titulo='titulo_serie', genero='genero_serie', temporadas ='3', entregada = False, creador = 'Creador_serie'):
        self.titulo = titulo
        self.genero = genero
        self.temporadas = temporadas
        self.entregada = entregada
        self.creador = creador

    def get_titulo(self):
        return self.titulo

    def get_genero(self):
        return self.genero

    def get_temporadas(self):
        return self.temporadas

    def get_creador(self):
        return self.creador

    def set_titulo(self,nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_genero(self,nuevo_genero):
        self.genero=nuevo_genero

    def set_temporadas(self,nuevo_temporadas):
        self.temporadas=nuevo_temporadas

    def set_creador(self,nuevo_creador):
        self.creador=nuevo_creador


    def __str__(self):
        return self.titulo

serie1 = Serie('Witcher' , 'Fantasia', '4', 'Henry C.')
serie2 = Serie('Sci-fi', 'A German guy.')