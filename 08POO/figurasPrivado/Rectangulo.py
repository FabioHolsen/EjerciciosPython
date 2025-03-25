class Rectangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura
    
    def getBase(self):
        return self.__base

    def setBase(self,valorBase):
        self.__base = valorBase

    def getAltura(self):
        return self.__altura

    def setAltura(self,valorAltura):
        self.__altura = valorAltura

    def perimetro(self):
        perimetroR = (self.getBase()*2)+(self.getAltura()*2)
        return perimetroR
    def area(self):
        areaR = self.getBase() * self.getAltura()
        return areaR