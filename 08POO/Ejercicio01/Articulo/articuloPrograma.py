from Articulo import *

articulo1 = Articulo("manzana",100,8)
articulo1.imprime()
print(articulo1.precioPVP())
print(articulo1.precioDescuento(21))
venta = int(input("Cuantos quieres comprar?: "))
vendio = articulo1.vender(venta)

if vendio == True:
    print(articulo1.getCuantosQuedan())

almacen = int(input("Cuantos quieres almacenar?: "))
articulo1.almacenar(almacen)
print(articulo1.getCuantosQuedan())