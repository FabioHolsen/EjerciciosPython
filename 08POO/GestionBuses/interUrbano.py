from Autobus import Autobus

class InterUrbano(Autobus):
    def __init__(self,matricula,plazas,km,conductor,paradas,ruta):
        super().__init__(matricula,plazas,km,conductor)
        self.__paradas = paradas
        self.__ruta = ruta

    def getParadas(self):
        return self.__paradas
    def setParadas(self,value):
        self.__paradas = value

    def getRuta(self):
        return self.__ruta
    def setRuta(self,value):
        self.__ruta = value

    def precioBillete(self):
        precio = 0
        if self.__ruta == "A":
            precio = 2
        elif self.__ruta == "B":
            precio = 4
        elif self.__ruta == "C":
            precio = 6
        return precio
    def mostrarAutoBus(self):
        super().mostrarAutobus()
        print(f"El numero de paradas es: {self.getParadas}")
        print(f"La ruta es: {self.getRuta}")
        print("El precio del billete es")