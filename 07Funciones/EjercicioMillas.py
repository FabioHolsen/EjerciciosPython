def numero():
    fin = False
    while not(fin):
        num = float(input("Inserte la distancia en millas: "))
        if num < 0:
            print("El numero tiene que ser mayor que 0.")
        else:
            fin = True
    return num
def cambio(x):
    cambio = x*1609.34
    return(cambio)

cam = numero()
metro = cambio(cam)
print(f"{cam} milla(s) son {metro} metros.")
    