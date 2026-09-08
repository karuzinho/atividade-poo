notas = {}
for numero in range(1, 4):
    notas[input(f"Nome do estudante {numero}: ")] = float(input("Nota final: "))
for nome, nota in notas.items():
    situacao = "Aprovado" if nota >= 7 else "Reprovado"
    print(f"{nome}: {nota:.1f} - {situacao}")
