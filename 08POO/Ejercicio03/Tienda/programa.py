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
        fin1 = False
        nSerie = input("Dime el no de Serie del ordenador: ")
        memoria = input("Dime la cantidad de memoria RAM del ordenador: ")
        carProce = input("Dime las caracteristicas del ordenador: ")
        so = input("Dime el sistema operativo: ")
        tienePrecio = input("¿Tiene precio? (s/n): ")
        while fin1 == False:
            if tienePrecio == "s":
                precio = float(input("Dime el precio: "))
                ordenador = Ordenador(nSerie,memoria,carProce,so,precio)
                fin1 = True
            elif tienePrecio == "n":
                ordenador = Ordenador(nSerie,memoria,carProce,so)
                fin1 = True
            else:
                print("Error. Vuelva a intentarlo.")
                fin1 = False
                tienePrecio = input("¿Tiene precio? (s/n): ")
        tienda.agregarOrdenador(ordenador)
    if opcion == 2:
        nSerie = input("Dime el no de Serie del ordenador: ")
        tienda.borrarOrdenador(nSerie)
    if opcion == 3:
        nSerieB = input("Dime el no de Serie del ordenador: ")
        ordenadorB = tienda.mostrarOrdenador(nSerieB)
        ordenadorB.mostrarPC()
    if opcion == 4:
        tienda.mostrarTienda()



