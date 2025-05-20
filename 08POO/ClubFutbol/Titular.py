from Jugador import Jugador
class Titular(Jugador):

    def __init__(self, nombre, edad, salario, posicion,partidos):
        super().__init__(nombre, edad, salario, posicion)
        self.__partidos = partidos

    def getPartidos(self):
        return self.__partidos
    def setPartidos(self,value):
        self.__partidos = value

    def mostrarTitular(self):
        self.mostrarJugador()