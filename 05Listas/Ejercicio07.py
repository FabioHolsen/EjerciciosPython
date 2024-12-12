abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
borrar = []
largo = len(abc)
for i in range(2,largo,3):
    borrar.append(abc[i])

for j in borrar:
    abc.remove(j)


print(abc)
