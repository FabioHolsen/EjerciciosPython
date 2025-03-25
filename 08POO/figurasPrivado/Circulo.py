from math import pi
class Circulo:
    def __init__(self,radio):
        self.__radio = radio

    def getRadio(self):
        return self.__radio
    
    def setRadio(self, valorRadio):
        self.__radio = valorRadio

    def perimetro(self):
        perimetroCirc = self.getRadio()*2*pi
        return perimetroCirc
    
    def area(self):
        areaCirc = pi*(self.getRadio()**2)
        return areaCirc