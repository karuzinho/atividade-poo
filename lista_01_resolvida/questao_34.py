from math import sqrt

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))
if a == 0:
    print("O coeficiente a deve ser diferente de zero.")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Não há raízes reais.")
    elif delta == 0:
        print(f"Raiz real: {-b / (2 * a):.2f}")
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"Raízes reais: {x1:.2f} e {x2:.2f}")
