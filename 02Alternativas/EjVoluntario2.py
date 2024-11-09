numero = int(input("Inserte un numero del 1 al 5: "))

match numero:
    case 1:
        print("uno")
    case 2:
        print("dos")
    case 3:
        print("tres")
    case 4:
        print("cuatro")
    case 5:
        print("cinco")
    case other: 
        print("Mientes.")