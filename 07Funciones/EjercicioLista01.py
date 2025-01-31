def leerNum(mensaje):
    n=int(input(f"{mensaje}"))
    return n

def llenarLista(nLista):
    num = leerNum("Cuantos numeros quieres en la lista?: ")
    for i in range(num):
        num2 = leerNum("Dame un numero: ")
        nLista.append(num2)
    return

def media(lista):
    sum = 0
    for i in lista:
         sum = sum + i
    return sum/len(lista)

listaNumeros = []
llenarLista(listaNumeros)
print(listaNumeros)
total = media(listaNumeros)
print(int(total))
