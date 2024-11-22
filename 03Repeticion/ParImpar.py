contPar = 0
contImpar = 0



for i in range (0,15):
    num = int(input(f"Dame un numero ({i}): "))
    if num % 2 == 0:
        contPar = contPar + 1
        print("Es par")
    else:
        contImpar = contImpar + 1
        print("Es impar")
print("")        
print("Fin del programa.")

print("")
print(f"Hay {contPar} numeros pares.")
print(f"Hay {contImpar} numeros impares.")


    
