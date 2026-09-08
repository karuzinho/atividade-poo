notas = [float(input(f"Nota do estudante {numero}: ")) for numero in range(1, 11)]
aprovados = sum(nota >= 7 for nota in notas)
print("Quantidade de aprovados:", aprovados)
