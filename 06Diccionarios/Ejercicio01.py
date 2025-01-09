divisa = {"Euro":"€","Dolar":"$","Yen":"¥"}


seguir = True
while seguir:
    pregunta = input("Dime una divisa: ")
    simbolo = divisa.get(pregunta,"No encontrado")
    print(simbolo)
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "n":
        seguir = False