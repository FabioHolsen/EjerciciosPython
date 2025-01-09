lista1 = []
lista2 = []
cant = int(input("Cuantos elementos tiene la lista: ")) 

for i in range(cant):
    objLista1 = input("Dime el equipo: ")
    lista1.append(objLista1)
    objLista2 = int(input("Dime la puntuación: "))
    lista2.append(objLista2)



for k in range(cant):
    for l in range(cant-1):
        if lista2[l] > lista2[l+1]:
            camb = lista2[l]
            lista2[l] = lista2[l+1]
            lista2[l+1] = camb

            camb1 = lista1[l]
            lista1[l] = lista1[l+1]
            lista1[l+1] = camb1

print(lista1)
print(lista2)
print("")
print("Equipos:")
print("")
lista1.reverse()
lista2.reverse()
for j in range(cant):
    print(f"{j+1}. {lista1[j]}: {lista2[j]} puntos.")