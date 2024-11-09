num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))
producto = int(input("Inserte elproducto de los numeros anteriores: "))
productoReal = num1*num2
if num1 * num2 == producto:
    print("El producto es correcto.")
else:
    print(f"El producto es incorrecto. El producto real es: {productoReal}")