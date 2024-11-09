fin = False

while( not fin):
    print("")
    print("Calculadora")
    print("")
    print("1. Suma.")
    print("2. Resta.")
    print("3. Multiplicación. ")
    print("4. División. ")
    print("5. Salir. ")
    print("")
    opcion = int(input("Dime la opcion: "))
    print("")
    if opcion > 5 or opcion < 1:
        print("Opcion incorrecta")
    elif opcion == 5:
        print("Fin del programa.")
        fin = True
    else:
        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))
        print("")
        match opcion:
            case opcion if opcion == 1:
                suma = num1 + num2
                print(f"La suma es: {suma}")
            case opcion if opcion == 2:
                resta = num1 + num2
                print(f"")
            case opcion if opcion == 3:
                multi = num1 * num2
                print(f"La multiplicacion es: {multi}")
            case opcion if opcion == 4:
                if num2 == 0:
                    print("No puedes dividir entre 0.")
                else:
                    div = num1 / num2
                    print(f"La division es: {div}")

                          