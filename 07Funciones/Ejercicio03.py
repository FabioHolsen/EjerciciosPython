def factorial(x):
    res = 1
    for i in range(1,x+1):
        res = res * i
    return(res)
numero = int(input("Dime un numero: "))
resultado = factorial(numero)
print(f"El resultado es {resultado}")