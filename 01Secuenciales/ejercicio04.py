print("Dame un número")
x =  float(input())
print("Dame otro número")
y =  float(input())
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
divisionEntera = x // y
exponencial = x**y
resto = x % y
mayor = x > y
menor = x < y
print(f"Los números son: {x}, {y}")
print(f"{x} es mayor que {y}:", (mayor==True))
print(f"{x} es menor que {y}:", (menor==True))
print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicación es {multiplicacion}")
print(f"La división es {division}")
print(f"La división entera es {divisionEntera}")
print(f"El exponencial es {exponencial}")
print(f"El resto es {resto}")
