class PreparadorFisico:
    def __init__(self,nombre,exp):
        self.__nombre = nombre
        self.__exp = exp

    def getNombre(self):
        return self.__nombre
    def setNombre(self,value):
        self.__nombre = value

    def getExp(self):
        return self.__exp
    def setExp(self,value):
        self.__exp = value