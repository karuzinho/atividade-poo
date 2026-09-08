aluno_a = {item.strip() for item in input("Linguagens do aluno A (separe por vírgula): ").split(",") if item.strip()}
aluno_b = {item.strip() for item in input("Linguagens do aluno B (separe por vírgula): ").split(",") if item.strip()}
print("Aluno A:", aluno_a)
print("Aluno B:", aluno_b)
print("Em comum:", aluno_a & aluno_b)
print("Pelo menos um conhece:", aluno_a | aluno_b)
print("Apenas A:", aluno_a - aluno_b)
print("Quantidade de linguagens diferentes:", len(aluno_a | aluno_b))
