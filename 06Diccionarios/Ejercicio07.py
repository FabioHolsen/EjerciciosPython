cesta = {}
sigue = True
t = 0
while sigue == True:
    articulo = input("Dime el articulo: ")
    precio = float(input(f"Dime el precio de {articulo}: "))
    cesta[articulo] = precio
    t=t+precio

    fin=input("¿Desea continuar? (s/n)")
    if fin=="s":
        sigue = True
    else:
        sigue = False

print("Lista de la compra")
print("")
for i,j in cesta.items():
    print(f"{i} {j}")

print(f"Total {t}")