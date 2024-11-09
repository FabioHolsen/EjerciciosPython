print("Introduce el precio del articulo")
precioArt = float(input())
print("Introduce el precio de Venta")
precioVenta = float(input())
Descuento =((precioArt-precioVenta)*100)/precioArt
print(f"El descuento es", "%.2f"%Descuento)