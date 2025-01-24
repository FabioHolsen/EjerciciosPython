def tabla():
    fin = False
    while not(fin):
        numero = int(input("Dame un numero entre 1 y 10: "))
        if numero < 0 or numero > 11:
            print("Numero fuera del valor.")
        else:
            fin = True
    return numero
def multiplicacion(x):
    for i in range(1,11):
        print(f"{i} x {x} = {i*x}")

num = tabla()
multiplicacion(num)
