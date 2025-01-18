muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
muroL = len(muro)
laberintoM = []
for filaM in range(0,4):
    laberintoM.append([])
    print(laberintoM)

fila0 = []
fila1 = []
fila2 = []
fila3 = []
fila4 = []
laberinto = [fila0, fila1, fila2, fila3, fila4]
print(muroL)

for muroL in muro:
    if muroL[0] == 0:
        valorF0 = muroL[1]
        fila0.append(valorF0)
    elif muroL[0] == 1:
        valorF1 = muroL[1]
        fila1.append(valorF1)
    elif muroL[0] == 2:
        valorF2 = muroL[1]
        fila2.append(valorF2)
    elif muroL[0] == 3:
        valorF3 = muroL[1]
        fila3.append(valorF3)
    elif muroL[0] == 4:
        valorF4 = muroL[1]
        fila4.append(valorF4)
print(laberinto)
for i in laberinto:
    largo = len(i)
    print(type(largo))
    for j in range(largo):
         