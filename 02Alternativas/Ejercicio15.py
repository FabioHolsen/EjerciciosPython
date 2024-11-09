num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))

if num1 > num2:
    if num1 % num2 == 0:
        print(f"El numero menor {num2} es divisor del numero mayor {num1}.")
    else:
        print(f"El numero menor {num2} no es divisor del numero mayor {num1}.")
else:
    if num2 % num1 == 0:
        print(f"El numero menor {num1} es divisor del numero mayor {num2}.")
    else:
        print(f"El numero menor {num1} no es divisor del numero mayor {num2}.")
