muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
muroL = len(muro)
laberintoM = []
print(muroL)
for filaM in range(0,5):
    laberintoM.append([])
    for columnaM in range(0,5):
        laberintoM[filaM].append(" ")
for i in range(muroL):
    laberintoM[muro[i][0]][muro[i][1]] = "X"

print(laberintoM)