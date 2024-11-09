par = 0
impar = 0
for i in range(100,201):
    if (i%2==0):
        par = par + i
    else:
        impar = impar + i

print(f"La suma de los numeros pares es: {par}")
print(f"La suma de los numeros impares es: {impar}")