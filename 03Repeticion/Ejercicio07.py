num1 = int(input("Dime la cantidad de numeros que quieres introducir:"))
negativos = 0
for i  in range(1,num1+1,1):
    num2 = int(input("Dime el numero:"))
    if num2 < 0:
        negativos = negativos +1

positivos = num1 - negativos

print(" ")
print(f"Hay {negativos} numeros negativos")
print(f"Hay {positivos} numeros positivos") 