from Vehiculo import Vehiculo

class Monopatin(Vehiculo):
    def __init__(self,id,color,longitud,km,ruedas,potencia):
        super().__init__(id,color,longitud,km)
        self.__ruedas = ruedas
        self.__potencia = potencia

    def getRuedas(self):
        return self.__ruedas
    def setRuedas(self,value):
        self.__ruedas = value

    def getPotencia(self):
        return self.__potencia
    def setPotencia(self,value):
        self.__potencia = value

    def MostrarMonopatin(self):
        super().mostrarDatosVehiculos()
        print(f"Ruedas: {self.getRuedas()}")
        print(f"Potencia: {self.getPotencia()}")