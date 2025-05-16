from Vehiculo import Vehiculo
class ListaVehiculos:
    def __init__(self):
        self.__listaVehiculos=[]
    
    def anadirVehiculo(self,vehiculo):
        boolC = False
        if vehiculo != None:
            self.__listaVehiculos.append(vehiculo)
            boolC = True
        return boolC
    
    def buscarVehiculoPos(self,id):
        cont = 0
        encontrado = False
        pos = -1
        while cont < len(self.__listaVehiculos) and encontrado == False:
            vehiculo = self.__listaVehiculos[cont]
            if vehiculo.getId() == id:
                pos = cont
                encontrado = True
            cont = cont + 1
        return pos
    
    def buscarVehiculo(self,id):
        encontrado = False
        vehiculoEnc = None
        cont = 0
        while cont < len(self.__listaVehiculos) and encontrado == False:
            vehiculo = self.__listaVehiculos[cont]
            if vehiculo.getId() == id:
                encontrado = True
                vehiculoEnc = vehiculo
            cont = cont + 1
        return vehiculoEnc
    
    def eliminarVehiculo(self,id):
        pos = self.buscarVehiculoPos(id)
        if pos != -1:
            self.__listaVehiculos.pop(pos)
            print("Vehiculo eliminado correctamente.")
        else:
            print("Vehiculo no existe.")
    
    def  mostrarVehiculos(self):
        for i in self.__listaVehiculos:
            i.mostrarDatosVehiculo()

