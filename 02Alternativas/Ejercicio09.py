num1 = int(input("Inserte el primer numero:"))
num2 = int(input("Inserte el segundo numero:"))
num3 = int(input("Inserte el tercer numero:"))

if num1 == num2:
    if num1 == num3:
        print("Todos los numeros son iguales.")
    else:
        print(f"El primer numero y el segundo numero son iguales.")
elif num1 == num3:
     print(f"El primer numero y el tercer numero son iguales.")
elif num2 == num3:
    print(f"El segundo numero y el tercer numero son iguales.")
else:
    print("Todos los numeros son distintos.")