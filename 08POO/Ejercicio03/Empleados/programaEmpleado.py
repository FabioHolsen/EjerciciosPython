from Empleado import Empleado
listaE = []

def insertarEmpleado(nombre,horas,paga,lista):
    empleado = Empleado(nombre,horas,paga)
    lista.append(empleado)
def mostrarNomina(nombre,lista):
    cont = 0
    encontrado = False
    while cont < len(lista) and not encontrado:
        empleado = lista[cont]
        if empleado.getEmpleado() == nombre:
            print(f"Tu nomina es: {empleado.calculaNomina()} ")
            encontrado = True
        else:
            cont = cont + 1

def mostrarEmpleados(lista):
    for empleado in lista:
        empleado.mostrarEmpleado()

opciones =["1. Insertar un empleado","2. Mostrar la nomina del empleado","3. Mostrar un empleado","4. Mostrar todos los empleados","5. Salir"]
opcion = 0
while opcion != 5:
    for i in opciones:
        print(i)
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nombre1 = input("Dime el nombre del empleado: ")
        horas1 = int(input("Dime las horas que realiza el empleado: "))
        paga1 = float(input("Dime su paga por horas: "))
        insertarEmpleado(nombre1,horas1,paga1,listaE)
    elif opcion == 2:
        nombre2 = input("Dime el nombre del empleado: ")
        mostrarNomina(nombre2,listaE)
    elif opcion == 4:
        mostrarEmpleados(listaE)
