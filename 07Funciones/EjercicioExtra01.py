fin = False

def compra():
    fin = False
    listaArticulo = []
    listaTotal = []
    while not(fin):
        fin = False
        articulo = input("Dime el articulo: ")
        precioArticulo = float(input(f"Dime el precio de {articulo}: "))
        cantidad = int(input("Dime la cantidad que vas a comprar: "))
        listaArticulo.append(articulo)
        listaArticulo.append(precioArticulo)
        for i in range(0,cantidad):    
            listaTotal.append(listaArticulo)
        sigue = input("¿Desea seguir con la compra? (si/no): ")
        sigue = sigue.lower()
        if sigue == "si":
            fin = False
        elif sigue == "no":
            fin = True
    return listaTotal

def descuento(lista):
    semiT = 0
    descuentoF = 0
    for i in lista:
        semiT = semiT+ i[1]
    if semiT > 100:
        descuentoF = semiT*0.1
    return descuentoF

def semiTotal(lista):
    semi = 0
    for i in lista:
        semi = semi+ i[1]
    return semi

def precioFinal(lista, descuento):
    semiT = 0
    for i in lista:
        semiT = semiT+ i[1]
    return semiT - descuento
def ticketI(lista):
    for i in range(0,len(lista)):
        print(f"{i+1}. {lista[i][0]}: {lista[i][1]}")
while not(fin):
    listaT = compra()
    ticketI(listaT)
    descuentoT = descuento(listaT)
    semiT = semiTotal(listaT)
    total = precioFinal(listaT,descuentoT)
    print(f"El semitotal es: {semiT:.2f}€")
    print(f"El total es: {total:.2f}€")
    sigue = input("¿Desea seguir? (si/no): ")
    sigue = sigue.lower()
    if sigue == "si":
        fin = False
    elif sigue == "no":
        fin = True
