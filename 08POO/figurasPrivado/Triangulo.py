from math import *
class Triangulo:
    def __init__(self,lado):
        self.__lado = lado
        
    def getLado(self):
        return self.__lado

    def setLado(self,valorLado):
        self.__lado = valorLado


    def perimetro(self):
        perimetroC = self.getLado()*3
        return perimetroC

    def area(self):
        areaC = (self.getLado()**2)*sqrt(3)/4
        return areaC