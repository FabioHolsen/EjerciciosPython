def productos():
    listaProductos = []
    fin = False
    while not(fin):        
        producto = input("Dime el producto: ")
        precio = input("Dime el precio: ")       
        stock = int(input("Dime el stock: ")) 
        dicProducto = {"nombre":producto,"precio":precio+"€","stock":stock}
        seguir = input("¿Desea seguir? (s/n): ")
        seguir = seguir.lower()
        if seguir == "s":
            listaProductos.append(dicProducto)
            print(listaProductos)
            fin = False    
        elif seguir == "n":
            listaProductos.append(dicProducto)
            fin = True
        else:
            print("Error. Vuelva a ingresar el producto.")
            fin = False
    return  listaProductos

def checkP(listaP):
    fin = False
    existe = False
    while not(fin):
        productoC = input("Dime el producto a comprar: ")
        print(listaP)
        for i in range(0,len(listaP)):
            if listaP[i]["nombre"] == productoC:
                idProd = listaP[i]
                existe = True
        if existe == True:
            fin = True
            print(idProd)
        else:
            print("El producto no existe.")
            fin = False
    return idProd

def checkStock(prod):
    fin = False
    while not(fin):
        cant = int(input(f"Dime la cantidad de {prod["nombre"]} que quieres comprar: "))
        if  prod["stock"]>= cant:
            compra = {"producto":prod["nombre"],"cantidad":cant, "precio":prod["precio"]}
            fin = True
        else:
            print("No hay suficiente stock para realizar la compra.")
            compra = {"producto":prod["nombre"],"cantidad":0}
            fin = True    
    return compra

def compra(listaPr):
    fin = False
    listaCompra = []
    while not(fin):    
        producto = checkP(listaPr)
        articuloCompra = checkStock(producto)    
        listaCompra.append(articuloCompra)
        seguir = input("¿Desea seguir? (s/n): ")
        seguir = seguir.lower()
        if seguir == "s":
            fin = False  
        elif seguir == "n":
            fin = True
        else:
            print("Error.")
            fin = False
    return listaCompra

listaProc = productos()
listaCompra = compra(listaProc)
print(listaCompra)