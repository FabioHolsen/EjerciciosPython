print("MAYORES QUE EL PRIMERO")
print("")
val = int(input("¿Cuantos valores va a introducir?: "))
if val < 0:
    print("¡Imposible!")
elif val == 0:
    print("Fin del programa.")
else:
    num = int(input("Escriba un numero: "))
    for i in range(1,val):
        numMayor = int(input(f"Escriba un numero mas grande que {num}: "))
        if numMayor < num:
            print(f"¡{numMayor} no es mayor que {num}!")
    print("Gracias por su colaboración")