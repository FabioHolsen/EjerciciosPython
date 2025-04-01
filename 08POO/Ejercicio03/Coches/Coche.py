class Coche:
    def __init__(self,matricula,color,cilindrada,plazas,propietario=""):
            self.__matricula = matricula
            self.__color = color
            self.__cilindrada = cilindrada
            self.__plazas = plazas
            self.__propietario = propietario
    
    def getMatricula(self):
        return self.__matricula
    def setMatricula(self,value):
        self.__matricula = value
    
    def getColor(self):
        return self.__color
    def setColor(self,value):
        self.__color = value
    
    def getCilindrada(self):
        return self.__cilindrada
    def setCilindrada(self,value):
        self.__cilindrada = value
    
    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,value):
        self.__plazas = value
    
    def getPropietario(self):
        return self.__propietario
    def setPropietario(self,value):
        self.__propietario = value

    def muestraCoche(self):
        print(f"""Matricula: {self.getMatricula}\n
                Color: {self.getColor}\n
                Cilindrada: {self.getCilindrada}\n
                Plazas: {self.getPlazas}\n
                Propietario: {self.getPropietario}""")