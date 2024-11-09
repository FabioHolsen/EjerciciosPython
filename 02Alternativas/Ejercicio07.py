num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))
num3 = int(input("Inserte el tercer numero: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} es el mayor.")
    else:
        print(f"{num3} es el mayor.")
else:
    if num2 > num3:
        print(f"{num2} es el mayor.")
    else:
        print(f"{num3} es el mayor.")
