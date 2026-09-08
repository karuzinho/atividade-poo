inicio = int(input("Primeiro identificador: "))
fim = int(input("Último identificador: "))

numeros = range(min(inicio, fim), max(inicio, fim) + 1)
print(f"Média: {sum(numeros) / len(numeros):.2f}")
