persona = {}
sigue = True
while sigue== True:
    key = input("¿Que dato quieres guardar?: ")
    dato= input(f"Dime el {key}: ")
    persona[key]=dato
    print(persona)

    fin=input("¿Desea continuar? (s/n)")
    if fin=="s":
        sigue = True
    else:
        sigue = False