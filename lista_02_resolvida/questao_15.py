disciplina = {
    "nome": input("Nome da disciplina: "),
    "professor": input("Professor: "),
    "carga_horaria": input("Carga horária: "),
    "quantidade_alunos": input("Quantidade de alunos: "),
    "situacao": input("Situação: "),
}
for chave, valor in disciplina.items():
    print(f"{chave}: {valor}")
