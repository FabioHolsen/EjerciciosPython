num = int(input("Dime el numero: "))
numWhile = num
print("Con for:")
for i  in range(num,-1, -1):
    print(i)
print("Con While:")    
while numWhile != -1:
    print(numWhile)
    numWhile = numWhile -1
    
