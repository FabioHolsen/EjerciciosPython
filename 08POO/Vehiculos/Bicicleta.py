class Bicicleta:
    def __init__(self,id,color,longitud,km,tipo,motor):
        self.__id = id
        self.__color = color
        self.__longitud = longitud
        self.__km = km
        self.__tipo = tipo
        self.__motor = motor

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
    
    def getTipo(self):
        return self.__tipo
    def setTipo(self,value):
        self.__tipo = value

    def getMotor(self):
        return self.__motor
    def setMotor(self,value):
        self.__motor = value

    def mostrarBicicleta(self):
        print(f"La bicicleta con ID: {self.getId()} es:")
        print(f"Color: {self.getColor()}")
        print(f"Longitud: {self.getLongitud()}")
        print(f"Km: {self.getKm()}")
        print(f"Tipo: {self.getTipo()}")
        print(f"Motor: {self.getMotor()}")