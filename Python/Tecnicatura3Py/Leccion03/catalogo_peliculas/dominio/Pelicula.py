#Clase 3 Parte 2 Python
class Pelicula:
    def __int__(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self.nombre}'

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre ):
        self._nombre =nombre
