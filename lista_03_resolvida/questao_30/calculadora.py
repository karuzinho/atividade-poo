from calc import adicionar, subtrair, multiplicar, dividir, potencia, resto

operacoes = {
    "1": ("Adição", adicionar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir),
    "5": ("Potência", potencia),
    "6": ("Resto da divisão", resto),
}

print("1-Adição  2-Subtração  3-Multiplicação  4-Divisão  5-Potência  6-Resto")
opcao = input("Operação: ")
if opcao in operacoes:
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    try:
        print(f"{operacoes[opcao][0]}: {operacoes[opcao][1](a, b)}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")
