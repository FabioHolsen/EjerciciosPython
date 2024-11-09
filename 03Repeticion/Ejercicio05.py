num = int(input("Dame un numero: "))
pFact = 1
for i in range(1,num+1,1):
    pFact = pFact * i

print(f"{num}! = {pFact}")