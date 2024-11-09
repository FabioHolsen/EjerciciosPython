import math
x = float(input("Inserte el precio de la compra: "))
descuento = x * 0.15
precioFinal = x - descuento

print(f"El precio final es ", "%.2f"%precioFinal)

