class Representante:
    def __init__(self,nombre,comision):
        self.__nombre = nombre
        self.__comision = comision

    def getNombre(self):
        return self.__nombre
    def setNombre(self,value):
        self.__nombre = value

    def getComision(self):
        return self.__comision
    def setComision(self,value):
        self.__comision = value

    def mostrarRepresentante(self):
        print(f"El nombre del representante es: {self.getNombre}")
        print(f"Su porcentaje de comision es: {self.getComision}")