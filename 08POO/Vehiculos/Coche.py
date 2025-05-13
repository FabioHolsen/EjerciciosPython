class Coche:
    def __init__(self,id,color,longitud,km,combustible,plazas,cilindrada):
        self.__id = id
        self.__color = color
        self.__longitud = longitud
        self.__km = km
        self.__combustible = combustible
        self.__plazas = plazas
        self.__cilindrada = cilindrada

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
        print(f"El coche con ID: {self.getId()} es:")
        print(f"Color: {self.getColor()}")
        print(f"Longitud: {self.getLongitud()}")
        print(f"Km: {self.getKm()}")
        print(f"Combustible: {self.getCombustible()}")
        print(f"Plazas: {self.getPlazas()}")
        print(f"Cilindrada: {self.getCilindrada()}")