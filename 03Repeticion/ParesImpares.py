repBool = True
repetir = None
while repBool == True: 

    num = int(input("Escribe un numero entero: "))
    numMayor = int(input(f"Escribe un numero entero mayor igual que {num}: "))
    
    while numMayor < num:
        print(f"¡Le he pedido un numero entero mayor o igual que {num}!")
        numMayor = int(input(f"Escribe un numero entero mayor igual que {num}: "))
    
    for i in range(num,numMayor+1):
        if i % 2 == 0:
            print(f"El numero {i} es par")
        else:
            print(f"El numero {i} es impar")
    repetir = None
    while repetir != "s" and repetir != "n":
        
        repetir = input("¿Quiere volver a ejecutar? s/n: ")
        
        if repetir == "s":
            repBool = True
        elif repetir == "n":
            repBool = False
             
