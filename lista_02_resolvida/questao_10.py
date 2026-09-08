estudante = {
    "nome": input("Nome: "),
    "matricula": input("Matrícula: "),
    "idade": int(input("Idade: ")),
    "curso": input("Curso: "),
    "semestre": int(input("Semestre: ")),
}
for chave, valor in estudante.items():
    print(f"{chave.capitalize()}: {valor}")
