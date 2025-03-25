class Libro:
    def __init__(self, titulo, autor, editorial, anyoPub=0,ISBN="",precio=0,numLibros=1,numPres=0):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__publicacion = anyoPub
        self.__ISBN = ISBN
        self.__precio = precio
        self.__numLibros = numLibros
        self.__numPrestados = numPres

    def getTitulo(self):
        return self.__titulo
    def setTitulo(self,value):
        self.__titulo = value

    def getAutor(self):
        return self.__autor
    def setAutor(self, value):
        self.__autor = value
    
    def getEditorial(self):
        return self.__editorial
    def setEditorial(self, value):
        self.__editorial = value

    def getPublicacion(self):
        return self.__publicacion
    def setPublicacion(self,value):
        self.__publicacion = value

    def getISBN(self):
        return self.__ISBN
    def setISBN(self,value):
        self.__ISBN = value

    def getPrecio(self):
        return self.__precio
    def setPrecio(self,value):
        self.__precio = value

    def getNumLibros(self):
        return self.__numLibros
    def setNumLibros(self,value):
        self.__numLibros = value

    def getNumPrestados(self):
        return self.__numPrestados
    def setNumPrestados(self,value):
        return self.__numPrestados
    
    def mostrarLibro(self):
        print(f"Titulo: {self.getTitulo()} Autor: {self.getAutor()} Ejemplares: {self.getNumLibros()} Prestados: {self.getNumPrestados()}" )