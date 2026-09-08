notas = [float(input(f"Nota {numero}: ")) for numero in range(1, 6)]
try:
    print("Todas as notas:", notas)
    print(f"Média: {sum(notas) / len(notas):.2f}")
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))
except ValueError:
    print("Não há notas para analisar.")
