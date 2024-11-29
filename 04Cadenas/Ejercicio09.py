lista = input("Dame la lista de la compra:")
lista = lista + ","
coma = lista.count(",")

if len(lista) > 0:
    inicio = 0
    for i in range(coma):
        pos = lista.find(",",inicio)
        producto = lista[inicio:pos]
        inicio = pos+1
        
        print(producto)

print("----------------------------------")

listaS = lista.split(",")

for i in range(0,coma):
    print(listaS[i])