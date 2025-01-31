def leerNum(mensaje):
    n=int(input(f"{mensaje}"))
    return n

def llenarLista(nLista):
    num = leerNum("Cuantas notas quieres en la lista?: ")
    for i in range(num):
        num2 = leerNum("Dame una nota: ")
        nLista.append(num2)
    return
def calificacion(n):
    cal=""
    if n < 3:
        cal = "Muy deficiente"
    elif n < 5:
        cal = "Insuficiente"
    elif n < 6:
        cal = "Suficiente"
    elif n < 7:
        cal = "Bien"
    elif n < 9:
        cal = "Notable"
    else:
        cal = "Sobresaliente"
    return cal

def calificaciones(calif):
    listaC = []
    for i in calif:
        nota = calificacion(i)
        listaC.append(nota)
    return listaC
listaNumeros = []
llenarLista(listaNumeros)
print(listaNumeros)
notasF =calificaciones(listaNumeros)
print(notasF)