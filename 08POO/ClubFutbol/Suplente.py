from Jugador import Jugador
class Suplente(Jugador):

    def __init__(self, nombre, edad, salario, posicion,entrenamientos):
        super().__init__(nombre, edad, salario, posicion)
        self.__entrenamientos = entrenamientos

    def getEntrenamientos(self):
        return self.__entrenamientos
    def setEntrenamientos(self,value):
        self.__entrenamientos = value

    def mostrarTitular(self):
        self.mostrarJugador()