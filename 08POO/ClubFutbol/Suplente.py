from Jugador import Jugador
class Suplente(Jugador):

    def __init__(self, nombre, edad, salario, posicion,representante,preparadorFisico,entrenamientos):
        super().__init__(nombre, edad, salario, posicion,representante,preparadorFisico)
        self.__entrenamientos = entrenamientos

    def getEntrenamientos(self):
        return self.__entrenamientos
    def setEntrenamientos(self,value):
        self.__entrenamientos = value

    def CalcularSalario(self):
        sueldo = (self.getSalario() * 0.7) + (10*self.getEntrenamientos())
        if self.getPreparadorFisico().getExp() > 10:      
            sueldo = sueldo + 200
        return sueldo

    def mostrarRol(self):
        self.mostrarJugador()
        print(f"El sueldo es: {self.CalcularSalario}")