class Vehiculo:
    def __init__(self,id,color,longitud,km):
        self.__id = id
        self.__color = color
        self.__longitud = longitud
        self.__km = km
        
    def getId(self):
        return self.__id
    def setId(self,value):
        self.__id = value

    def getColor(self):
        return self.__color
    def setColor(self,value):
        self.__color = value

    def getLongitud(self):
        return self.__longitud
    def setLongitud(self,value):
        self.__longitud = value

    def getKm(self):
        return self.__km
    def setKm(self,value):
        self.__km = value

    def mostrarDatosVehiculo(self):
        print(f"El coche con ID: {self.getId()} es:")
        print(f"Color: {self.getColor()}")
        print(f"Longitud: {self.getLongitud()}")
        print(f"Km: {self.getKm()}")