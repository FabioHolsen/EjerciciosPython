from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self,id,color,longitud,km,tipo,motor):
        super().__init__(id,color,longitud,km)
        self.__tipo = tipo
        self.__motor = motor
    
    def getTipo(self):
        return self.__tipo
    def setTipo(self,value):
        self.__tipo = value

    def getMotor(self):
        return self.__motor
    def setMotor(self,value):
        self.__motor = value

    def mostrarBicicleta(self):
        super().mostrarDatosVehiculo()
        print(f"Tipo: {self.getTipo()}")
        print(f"Motor: {self.getMotor()}")