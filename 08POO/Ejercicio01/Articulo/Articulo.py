class Articulo():
    __iva = 21
    def __init__(self,nombre,precio,cuantosQuedan):
        self.__nombre = nombre
        self.__precio = precio
        self.__cuantosQuedan = cuantosQuedan

    def getNombre(self):
        return self.__nombre
    def setNombre(self,value):
        self.__nombre = value

    def getPrecio(self):
        return self.__precio
    def setPrecio(self,value):
        self.__precio = value

    def getIva():
        return Articulo.__iva
    # def setIva(self,value):
    #     self.__iva = value
    
    def getCuantosQuedan(self):
        return self.__cuantosQuedan
    def setCuantosQuedan(self,value):
        self.__cuantosQuedan = value

    def imprime(self):
        print(f"El nombre del producto es: {self.getNombre()}")
        print(f"El iva del producto es: {Articulo.getIva()}")
        print(f"El precio del producto es: {self.getPrecio()}")
        print(f"La cantidad restante del producto es: {self.getCuantosQuedan()}")

    def precioPVP(self):
        resultado=self.getPrecio()*(Articulo.getIva()/100)
        return self.getPrecio() + resultado
    
    def precioDescuento(self,dto):
        descuento = (self.precioPVP()*(dto/100))
        return self.precioPVP() - descuento
    
    def vender(self,cant):
        if self.getCuantosQuedan() < cant:
            venta = False
            print("Articulos insuficientes")
        else:
            venta = True
            self.setCuantosQuedan(self.getCuantosQuedan()-cant)
        return venta
    def almacenar(self,cant):
        self.setCuantosQuedan(self.getCuantosQuedan()+cant)