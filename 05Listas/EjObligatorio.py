import random


equipos = []
ganadorR1 = []
ganadorR2 = []
resultado = ["L","V"]
for eq in range(8):
    equipo = input(f"Dime el nombre del equipo({eq+1}): ")
    equipos.append(equipo)
    equiposI = equipos
print(" ")

for prEquipo in range(len(equipos)):
    print(f"Equipo {prEquipo+1}: {equipos[prEquipo]}")
print("")

eqRonda1L = []
eqRonda1V = []
contR1 = 7
for r1 in range(4):
    alSorteoR1L = random.randint(0,contR1)
    eqRonda1L.append(equipos[alSorteoR1L])
    equipos.pop(alSorteoR1L)
    alSorteoR1V = random.randint(0,contR1-1)   
    eqRonda1V.append(equipos[alSorteoR1V])
    equipos.pop(alSorteoR1V)
    contR1 = contR1 -2
print("Ronda 1")
print("")
for pr1 in range(4):
    alGanadorR1 = random.randint(0,1)     
    print(f"L. {eqRonda1L[pr1]} - V. {eqRonda1V[pr1]}: {resultado[alGanadorR1]} ")
    if resultado[alGanadorR1] == "L":
        ganadorR1.append(eqRonda1L[pr1])
    else:
        ganadorR1.append(eqRonda1V[pr1])

print("")
eqRonda2L = []
eqRonda2V = []
contR2 = 3
for r2 in range(2):
    alSorteoR2L = random.randint(0,contR2)
    eqRonda2L.append(ganadorR1[alSorteoR2L])
    ganadorR1.pop(alSorteoR2L)
    alSorteoR2V = random.randint(0,contR2-1)
    eqRonda2V.append(ganadorR1[alSorteoR2V])
    ganadorR1.pop(alSorteoR2V)
    contR2 = contR2 -2
print("Ronda 2")
print(" ")
for pr2 in range(2):
    alGanadorR2 = random.randint(0,1)     
    print(f"L. {eqRonda2L[pr2]} - V. {eqRonda2V[pr2]}: {resultado[alGanadorR2]} ")
    if resultado[alGanadorR2] == "L":
        ganadorR2.append(eqRonda2L[pr2])
    else:
        ganadorR2.append(eqRonda2V[pr2])
print("")
print("Ronda 3")
print("")
random.shuffle(ganadorR2)
alGanadorR3 = random.randint(0,1)
print(f"L. {ganadorR2[0]} - V. {ganadorR2[1]}: {resultado[alGanadorR3]}")
if resultado[alGanadorR3] == "L":
    campeon = ganadorR2[0]
else:
    campeon = ganadorR2[1]
print("")
print(f"Campeón: {campeon}")



