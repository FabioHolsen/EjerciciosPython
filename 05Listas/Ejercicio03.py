lista = ["Programación", "Lenguaje de Marcas", "Bases de datos"]
listaNota = []
cantLista = len(lista)
for i in lista:
        nota = int(input((f"¿Que nota has sacado en {i}?: ")))
        while nota <= -1 or nota >= 11: 
            print("Nota incorrecta.")
            nota = int(input((f"¿Que nota has sacado en {i}?: ")))
        listaNota.append(nota)
print("""
Resumen:
""")
for i in range(cantLista):
        print(f"Haz sacado {listaNota[i]} en {lista[i]}.")