class Jugador:
    def __init__(self,nombre,edad,salario,posicion):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario
        self.__posicion = posicion

    def getNombre(self):
        return self.__nombre
    def setNombre(self,value):
        self.__nombre = value

    def getEdad(self):
        return self.__edad
    def setEdad(self,value):
        self.__edad = value

    def getSalario(self):
        return self.__salario
    def setSalario(self,value):
        self.__salario = value

    def getPosicion(self):
        return self.__posicion
    def setPosicion(self,value):
        self.__posicion = value

    def mostrarJugador(self):
        print(f"El jugador {self.getNombre} tiene las siguientes caracteristicas:")
        print(f"Edad: {self.getEdad}")
        print(f"Posicion: {self.getPosicion}")