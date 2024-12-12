cursos = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notaLista = []
cursosR = []
largo = len(cursos)

for i in range(largo):
    nota = int(input(f"Dime la nota de {cursos[i]}: "))
    notaLista.append(nota)

for j in range(largo):
    if notaLista[j] <= 4:
        cursosR.append(cursos[j])

print(f"Cursos repetidos: {cursosR}")