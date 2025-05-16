class Autobus():
    def __init__(self,matricula,plazas,km,conductor):
        self.__matricula = matricula
        self.__plazas = plazas
        self.__km = km
        self.__conductor= conductor

    def getMatricula(self):
        return self.__matricula
    def setMatricula(self,value):
        self.__matricula = value
    
    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,value):
        self.__plazas = value
    
    def getKm(self):
        return self.__km
    def setKm(self,value):
        self.__km = value
    
    def getConductor(self):
        return self.__conductor
    def setConductor(self,value):
        self.__conductor = value

    def mostrarAutobus(self):
        print("Los datos del vehichulo son:")
        print(f"La matricula es: {self.getMatricula}")
        print(f"El numero de plazas es: {self.getPlazas}")
        print(f"Los kilometros son: {self.getKm}")
        print(f"El conductor es: {self.getConductor}")
