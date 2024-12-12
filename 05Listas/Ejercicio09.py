articulo = []
precio = []
for i in range(3):
    articuloN = input("Ingresa el nombre del articulo: ")
    articulo.append(articuloN)
    precioN = int(input("Ingresa el precio del articulo: "))
    precio.append(precioN)

precioMax = max(precio)
celdaPMax = precio.index(precioMax)
precioMin = min(precio)
celdaPMin = precio.index(precioMin)

print(f"El articulo con el mayor precio es: {articulo[celdaPMax]} con {precioMax} Euros.")
print(f"El articulo con el menor precio es: {articulo[celdaPMin]} con {precioMin} Euros.")