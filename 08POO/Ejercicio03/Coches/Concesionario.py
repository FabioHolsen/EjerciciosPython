from Coche import Coche

def cambiarColor(lista,mat,color):
    cont= 0
    encontrado = False
    while cont < len(lista) and encontrado == False:
        coche = lista[cont]
        if coche.getMatricula() == mat:
            coche.setColor(color)
            print("Coche pintado correctamente.")
            encontrado = True
        else:
            cont = cont + 1
def mostrarCoches(lista):
    for i in lista:
        i.muestraCoche()

concesionario = []

opciones =["1. Crea el coche","2. Vende el coche","3. Pinta el coche","4. Muestra coche","5. Muestra todos los coches","6. Salir"]
opcion = 0
while opcion != 6:
    for i in opciones:
        print(i)
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        mat=input("Introduce la matricula: ")
        col=input("Introduce el color: ")
        cilindrada=int(input("Introduce la cilindrada: "))
        plaza=int(input("Introduce el numero de plazas: "))
        prop=input("Introduce el propietario: ")
        coche=Coche(mat,col,cilindrada,plaza,prop)
        concesionario.append(coche)
        print("Coche creado correctamente.")
        print("")
    elif opcion == 2:
        matEl=input("Dime la matricula del vehiculo a vender: ")
        cont = 0
        encontrado = False
        while cont < len(concesionario) and encontrado == False:
            coche = concesionario[cont]
            if coche.getMatricula() == matEl:
                print("Encontrado.")
                encontrado = True
                concesionario.pop(cont)
            else:
                cont=cont+1
        if not encontrado:
            print("Error. Coche no encontrado.")
    elif opcion == 3:
        matC = input("Dime la matricula del coche: ")
        col = input("Dime el nuevo color: ")
        cambiarColor(concesionario,matC,col)
    elif opcion == 4:
        cont = 0
        encontrado = False
        matM = input("Dime la matricula del coche: ")
        while cont < len(concesionario) and encontrado == False:
            coche = concesionario[cont]
            if coche.getMatricula() == matM:
                print("Encontrado")
                print("")
                coche.muestraCoche()
                encontrado = True
            else:
                cont = cont + 1
    elif opcion == 5:
        mostrarCoches(concesionario)