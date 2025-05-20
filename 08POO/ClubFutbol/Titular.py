from Jugador import Jugador
class Titular(Jugador):

    def __init__(self, nombre, edad, salario, posicion,representante,preparadorFisico,partidos):
        super().__init__(nombre, edad, salario, posicion,representante,preparadorFisico)
        self.__partidos = partidos

    def getPartidos(self):
        return self.__partidos
    def setPartidos(self,value):
        self.__partidos = value

    def CalcularSalario(self):
        sueldo = self.getSalario() + (100*self.getPartidos())
        if self.getRepresentante().getComision() > 0.15:      
            sueldo = sueldo * 0.97
        return sueldo
    def mostrarRol(self):
        self.mostrarJugador()
        print(f"El sueldo es: {self.CalcularSalario}")