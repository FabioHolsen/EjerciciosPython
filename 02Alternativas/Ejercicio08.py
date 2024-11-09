nota = float(input("Dame tu nota: "))


if nota >= 0 and nota < 3:
    print("%.2f"%nota, "es deficiente.")
elif nota >=3 and nota < 5:
    print("%.2f"%nota, "es insuficiente.")
elif nota >=5 and nota < 6:
    print("%.2f"%nota, "es suficiente.")
elif nota >=6 and nota < 7:
    print("%.2f"%nota, "es bien.")
elif nota >=7 and nota < 9:
    print("%.2f"%nota, "es notable.")
else:
    print("%.2f"%nota, "es sobresaliente.")