producto = input("Dime el articulo, precio y cantidad(,): ")

listaP = producto.split(",")

nomArt = listaP[0]
precioArt = float(listaP[1])
cantidad = float(listaP[2])

print(precioArt*cantidad)
