muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
muroL = len(muro)
laberintoM = []
historial = []
ubicacion = [0,0]
fin = False
juego = False
for filaM in range(0,5):
    laberintoM.append([])
    for columnaM in range(0,5):
        laberintoM[filaM].append("   ")
for i in range(muroL):
    laberintoM[muro[i][0]][muro[i][1]] = "[X]"
laberintoM[4][4] = "[S]"
# for x in laberintoM:
#         for y in x:
#             print(y,end=" ")
#         print()
while not(fin):
    print('Escapa del laberinto')
    inicio = input("Desea empezar? s/n: ")
    if inicio == "s":
        
        while not(juego):
            
            laberintoM[ubicacion[0]][ubicacion[1]] = "[.]"
            for x in laberintoM:
                for y in x:
                    print(y,end=" ")
                print()
            direccion = input("Escoje una dirección: arriba/abajo/derecha/izquierda: ")
            if direccion == "arriba":
                if ubicacion[0] == 0:
                    print("No puedes subir más!")
                    historial.append("arriba")
                elif laberintoM[ubicacion[0]-1][ubicacion[1]] == "[X]":
                    print("No puedes pasar por aqui!")
                    historial.append("arriba")
                else:
                    ubicacion[0] = ubicacion[0] - 1
                    laberintoM[ubicacion[0]+1][ubicacion[1]] = "   "
                    print(ubicacion)
                    historial.append("arriba")
            if direccion == "abajo":
                if ubicacion[0] == 4:
                    print("No puedes bajar más!")
                    historial.append("abajo")
                elif laberintoM[ubicacion[0]+1][ubicacion[1]] == "[X]":
                    print("No puedes pasar por aqui!")
                    historial.append("abajo")
                else:
                    ubicacion[0] = ubicacion[0] + 1
                    laberintoM[ubicacion[0]-1][ubicacion[1]] = "   "
                    print(ubicacion)
                    historial.append("abajo")
            if direccion == "derecha":
                if ubicacion[1] == 4:
                    print("No puedes ir más a la derecha!")
                    historial.append("derecha")
                elif laberintoM[ubicacion[0]][ubicacion[1]+1] == "[X]":
                    print("No puedes pasar por aqui!")
                    historial.append("derecha")
                else:
                    ubicacion[1] = ubicacion[1] + 1
                    laberintoM[ubicacion[0]][ubicacion[1]-1] = "   "
                    print(ubicacion)
                    historial.append("derecha")
            if direccion == "izquierda":
                if ubicacion[1] == 0:
                    print("No puedes ir más a la izquierda!")
                    historial.append("izquierda")
                elif laberintoM[ubicacion[0]][ubicacion[1]-1] == "[X]":
                    print("No puedes pasar por aqui!")
                    historial.append("izquierda")
                else:
                    ubicacion[1] = ubicacion[1] - 1
                    laberintoM[ubicacion[0]][ubicacion[1]+1] = "   "
                    print(ubicacion)
                    historial.append("izquierda")
            if ubicacion[0] == 4 and ubicacion[1] == 4:
                juego = True
        print("Haz ganado!")
        print("Tu historial:")
        print(historial)
        fin = True
    else:
        fin = True
