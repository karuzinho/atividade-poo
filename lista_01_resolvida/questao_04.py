from math import sqrt

opcao = input("1-Hipotenusa | 2-Cateto: ")
if opcao == "1":
    cateto1 = float(input("Primeiro cateto: "))
    cateto2 = float(input("Segundo cateto: "))
    print(f"Hipotenusa: {sqrt(cateto1 ** 2 + cateto2 ** 2):.2f}")
elif opcao == "2":
    hipotenusa = float(input("Hipotenusa: "))
    cateto = float(input("Outro cateto: "))
    if hipotenusa > cateto:
        print(f"Cateto: {sqrt(hipotenusa ** 2 - cateto ** 2):.2f}")
    else:
        print("Valores inválidos.")
else:
    print("Opção inválida.")
