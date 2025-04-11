from Ordenador import *
from Tienda import *

tienda = Tienda("8406055","PcMorvedre","Juan Perez")

opcion = 0
menu = ["1. Añadir Ordenador","2. Eliminar Ordenador","3. Buscar Ordenador","4. Listar Ordenadores","5. Salir"]
while opcion != 5:
    for i in menu:
        print(i)
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        nSerie = input("Dime el no de Serie del ordenador: ")
        memoria = input("Dime la cantidad de memoria RAM del ordenador: ")
        carProce = input("Dime las caracteristicas del ordenador: ")
        so = input("Dime el sistema operativo: ")
        precio =input ("Dime el precio: ")
        if precio == "":
            ordenador = Ordenador(nSerie,memoria,carProce,so)
        elif so == "":
            precio = float(precio)
            ordenador = Ordenador(nSerie,memoria,carProce,precio=precio)
        elif precio == "" or so == "":
            ordenador = Ordenador(nSerie,memoria,carProce)
        else:
            ordenador = Ordenador(nSerie,memoria,carProce,so,precio)
        tienda.agregarOrdenador(ordenador)
    if opcion == 2:
        nSerie = input("Dime el no de Serie del ordenador: ")
        tienda.borrarOrdenador(nSerie)
    if opcion == 4:
        tienda.mostrarTienda()



