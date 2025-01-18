facturaL = {}
fin = False 
acciones = {1:"Añadir",2:"Pagar",3:"Mostrar"}
while not(fin):
    for i in acciones:
        print(f"{i}. {acciones.get(i)} facturas.")
    print("4. Salir.")
    opcion = int(input("Elige la opción: "))

    if opcion == 4:
        fin = True
    else:
        if opcion == 1:
            numfac = input("Dime el código de la factura: ")
            costfac = float(input("Dime el coste de la factura: "))
            facturaL[numfac] = costfac
        if opcion == 2:
            delFac = input("Dime el número de factura: ")
            if facturaL.get(delFac) == None:
                print("La factura no existe.")
            else:
                facturaL.pop(delFac)
                print("Factura borrada")
        if opcion == 3:
            print(facturaL) 
