precio = float(input("Inserte el precio del producto: "))

if precio < 6:
    precioFinal = precio
elif precio >= 6 and precio < 60:
    precioFinal = precio - (precio*0.05)
elif precio >=60:
    precioFinal = precio - (precio*0.10)

print(f"El precio final del producto es: ", "%.2f"%precioFinal, " Euros")