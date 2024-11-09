tarifa = float(input("Inserte su tarifa: "))
horasT = float(input("Inserte las horas trabajadas: "))

if horasT >= 35:
    sHorasExtra = (horasT-35)*tarifa*1.5
    sBruto = (35*tarifa)+sHorasExtra
else:
    sBruto = horasT*tarifa

if sBruto > 500:
    if sBruto > 900:
        tasa1=400*0.25
        tasa2=(sBruto-900)*0.45
        tasaT=tasa1+tasa2
    else:
        tasa1=(sBruto-500)*0.25
        tasaT=tasa1
else:
    tasaT = 0
sNeto=sBruto-tasaT

print(f"Sueldo bruto: ", "%.2f"%sBruto)
print(f"Tasa de impuesto: ", "%.2f"%tasaT)
print(f"Tu sueldo neto es: ", "%.2f"%sNeto)