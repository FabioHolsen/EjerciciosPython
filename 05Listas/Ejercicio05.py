lista = []
cont = 0
for i in range(10):
    cont = cont + 1
    lista.append(cont)

lista.sort(reverse=True)
print(lista)