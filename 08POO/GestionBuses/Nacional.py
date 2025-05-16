from Autobus import Autobus

class Nacional(Autobus):
    def __init__(self,matricula,plazas,km,conductor,distancia,tiempo):
        super().__init__(matricula,plazas,km,conductor)
        self.__distancia = distancia
        self.__tiempo = tiempo

    def getDistancia(self):
        return self.__distancia
    def setDistancia(self,value):
        self.__distancia = value

    def getTiempo(self):
        return self.__tiempo
    def setTiempo(self,value):
        self.__tiempo = value

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