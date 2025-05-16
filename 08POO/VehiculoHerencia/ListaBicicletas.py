from Bicicleta import Bicicleta
class ListaBicicletas:
    def __init__(self):
        self.__listaBicis=[]
    
    def anadirBicis(self,bicicleta):
        boolB = False
        if bicicleta != None:
            self.__listaBicis.append(bicicleta)
            boolB = True
        return boolB
    
    def buscarBiciPos(self,id):
        cont = 0
        encontrado = False
        pos = -1
        while cont < len(self.__listaBicis) and encontrado == False:
            bicicleta = self.__listaBicis[cont]
            if bicicleta.getId() == id:
                pos = cont
                encontrado = True
            cont = cont + 1
        return pos
    
    def buscarBici(self,id):
        encontrado = False
        biciEnc = None
        cont = 0
        while cont < len(self.__listaBicis) and not encontrado:
            bicicleta = self.__listaBicis[cont]
            if bicicleta.getId() == id:
                encontrado = True
                biciEnc = bicicleta
            cont = cont + 1
        return biciEnc
    
    def eliminarBici(self,id):
        pos = self.buscarBiciPos(id)
        if pos != -1:
            self.__listaBicis.pop(pos)
            print("Bicicleta eliminado correctamente.")
        else:
            print("Bicicleta no existe.")
    
    def  mostrarBicis(self):
        for i in self.__listaBicis:
            i.mostrarBicicleta()

