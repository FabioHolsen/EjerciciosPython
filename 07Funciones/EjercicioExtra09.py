def notaAlumno(listaEstudiantes):
    fin = False
    while not(fin):
        alumno = input("Dime el nombre del alumno: ")
        notas = []
        pedirNota = False
        while not(pedirNota):
            print(notas)
            nota = int(input("Dime la nota: "))
            if nota <= 0 or nota >= 10:
                print("Error, numero incorrecto")
            else:
                seguir = input("¿Desea ingresar otra nota? (s/n): ")
                seguir = seguir.lower()
                if seguir == "s":
                    notas.append(nota)
                    pedirNota = False  
                elif seguir == "n":
                    notas.append(nota)
                    pedirNota = True
                else:
                    print("Error.")
                    pedirNota = False
        seguirAl = input("¿Desea insertar otro alumno? (s/n): ")
        seguirAl = seguirAl.lower()
        if seguirAl == "s":
            estudiante = {"nombre":alumno,"calificaciones":notas}
            listaEstudiantes.append(estudiante)
            fin = False  
        elif seguirAl == "n":
            estudiante = {"nombre":alumno,"calificaciones":notas}
            listaEstudiantes.append(estudiante)
            fin = True
        else:
            print("Error.")
            fin = False
    return

def resumenNotas(dicAl):
    notas = dicAl["calificaciones"]
    suma=0
    for i in notas:
        suma=suma+i
    media=suma/len(notas)
    mensaje=("Has reprobado el curso")
    mensaje2 = (".")
    if media >=6:
        mensaje=("Haz aprobado el curso")
    if media >=9:
        mensaje2 = ". Eres un chico excelente."
    return media,mensaje,mensaje2

listaE = []
notaAlumno(listaE)
print(listaE)
# for i in listaE:
#     media, mensaje,mensaje2 = resumenNotas(i)
#     print(f"{i["nombre"]}, tu nota media es de {media}. {mensaje}{mensaje2}")
nomConsulta = input("Dime el nombre del alumno: ")
existe = False
for j in listaE:
    if j["nombre"] == nomConsulta:
        existe = True
        media, mensaje,mensaje2 = resumenNotas(j)
        print(f"{j["nombre"]}, tu nota media es de {media}. {mensaje}{mensaje2}")
if existe == False:
    print("No existe el alumno.")
