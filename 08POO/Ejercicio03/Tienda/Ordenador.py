class Ordenador:
    def __init__(self,nSerie,ram,cProcesador,os="Sin precio",precio=0.0):
        self._nSerie = nSerie
        self._ram = ram
        self._cProcesador = cProcesador
        self._os = os
        self._precio = precio

    def getNSerie(self):
        return self._nSerie
    def setNSerie(self,value):
        self._nSerie = value

    def getRam(self):
        return self._ram
    def setRam(self,value):
        self._ram = value

    def getCProcesador(self):
        return self._cProcesador
    def setCProcesador(self,value):
        self._cProcesador = value

    def getPrecio(self):
        return self._precio
    def setPrecio (self,value):
        self._precio = value

    def getOs(self):
        return self._os
    def setOs(self,value):
        self._os = value
    
    def mostrarPC(self):
        print(f"El ordenador con:\nNumero de serie: {self.getNSerie()}\nMemoria RAM: {self.getRam()}\nCaracteristicas del procesador: {self.getCProcesador()}\nSistema Operativo: {self.getOs()}\nPrecio: {self.getPrecio()}")
