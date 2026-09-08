numero = int(input("Número entre 1 e 10: "))

if 1 <= numero <= 10:
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
else:
    print("Número inválido.")
