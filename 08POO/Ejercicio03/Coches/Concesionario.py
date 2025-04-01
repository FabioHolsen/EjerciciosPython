from Coche import Coche
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
    elif opcion == 5:
        for i in concesionario:
            print(i.getMatricula())