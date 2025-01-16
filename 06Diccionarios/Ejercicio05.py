Creditos = {'Programacion':6,'Lenguaje de Marcas':4,'Sistemas Informaticos':5}
t=0
for nombre,credito in Creditos.items():
    print(f"{nombre} tiene {credito} créditos, donde {nombre} es cada una de las asignaturas del curso, y {credito} son sus créditos.")
    t=t+credito
print(f"El total de creditos es {t}")