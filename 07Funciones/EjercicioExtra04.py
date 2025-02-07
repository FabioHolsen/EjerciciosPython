def articulo():
    fin = False
    while not(fin):
        fin = False
        while not fin:
            num = int(input(f"Dime el precio del articulo: "))
            if num < 0:
                print("Valor incorrecto.")
            else:
                fin = True
    return num

def tarjeta(saldo,compra):
    if compra>saldo:
        msg="No tienes suficiente saldo"
    else:
        msg="Compra correcta"
        saldo = saldo - compra
    return saldo, msg
saldo=1000
compra= articulo()
resultado, mensaje = tarjeta(saldo,compra)
print(f"Saldo: {resultado} mensaje: {mensaje}")