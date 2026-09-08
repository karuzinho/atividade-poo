idade = int(input("Idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 18:
    print("Adolescente.")
else:
    print("Adulto.")
