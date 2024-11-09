numA = float(input("Dime el numero: "))
numB = int(input("Dime el exponente: "))
resultado = 1
for i in range(1,numB+1):
    resultado = resultado * numA
print(resultado)