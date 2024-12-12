vocal = ["a","e","i","o","u"]
palabra = input("Dime un palabra: ")

for i in vocal:
    contar = palabra.count(i)
    print(f"{i} sale {contar} veces.")


