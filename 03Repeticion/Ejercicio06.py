num1 = int(input("Dime la cantidad de numeros que quieres introducir:"))
Negativo = False
for i  in range(1,num1+1,1):
    num2 = int(input("Dime el numero:"))
    if num2 < 0:
        Negativo = True

if Negativo == True:
    print("Hay un numero negativo")
else:
    print("Hay un numero positivo")