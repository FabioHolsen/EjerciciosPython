from Vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self,id,color,longitud,km,combustible,plazas,cilindrada):
        super().__init__(id,color,longitud,km)  
        self.__combustible = combustible
        self.__plazas = plazas
        self.__cilindrada = cilindrada

    def getCombustible(self):
        return self.__combustible
    def setCombustible(self,value):
        self.__combustible = value

    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,value):
        self.__plazas = value
    
    def getCilindrada(self):
        return self.__cilindrada
    def setCilindrada(self,value):
        self.__cilindrada = value

    def mostrarCoche(self):
        super().mostrarDatosVehiculo()
        print(f"Combustible: {self.getCombustible()}")
        print(f"Plazas: {self.getPlazas()}")
        print(f"Cilindrada: {self.getCilindrada()}")