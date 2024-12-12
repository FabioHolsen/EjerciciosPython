lista = []

for i in range(6):
    numero = int(input("Dime el numero: "))
    while numero < -1  or numero > 50:
        print("Ingresa un numero entre 0 y 49.")
        numero = int(input("Dime el numero: "))
    lista.append(numero)   
lista.sort()
print(lista)
