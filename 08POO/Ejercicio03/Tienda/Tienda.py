class Tienda:
    def __init__(self,cifTienda,nombre,propietario):
        self._cifTienda = cifTienda
        self._nombre = nombre
        self._propietario = propietario
        self._listaPC = []

    def getCifTienda(self):
        return self._cifTienda
    def setCifTienda(self,value):
        self._cifTienda = value

    def getNombre(self):
        return self._nombre
    def setNombre(self,value):
        self._nombre = value

    def getPropietario(self):
        return self._propietario
    def setPropietario(self,value):
        self._propietario = value
    
    def getOrdenador(self,nSerie):
        cont = 0
        existe = False
        pos = -1
        while cont < len(self._listaPC) and existe == False:
            ordenador = self._listaPC[cont]
            if ordenador.getNSerie() == nSerie:
                pos = cont
                existe = True
            cont = cont + 1    
        return pos
    
    def agregarOrdenador(self,ordenador):
        if ordenador != None:
            self._listaPC.append(ordenador)
            print("Ordenador agregado correctamente")
        return 0
    
    def borrarOrdenador(self,nSerie):
        pos = self.getOrdenador(nSerie)
        if pos != -1:
            self._listaPC.pop(pos)
            print("Ordenador eliminado correctamente.")
        else:
            print("Ordenador no existe.")

    def mostrarOrdenador(self,nSerie):
        pos = self.getOrdenador(nSerie)
        if pos != -1:
            ordenador = self._listaPC[pos]
        else:
            print("El ordenador no existe.")
        return ordenador


    def  mostrarTienda(self):
        print(f"Tienda con CIF: {self.getCifTienda()}")
        print(f"Nombre: {self.getNombre()}")
        print(f"Propietario: {self.getPropietario()}")
        for i in self._listaPC:
            i.mostrarPC()

    
    