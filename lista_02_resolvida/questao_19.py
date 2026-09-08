boletim = {}
for numero in range(1, 4):
    nome = input(f"Nome do estudante {numero}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    boletim[nome] = {"nota_1": nota1, "nota_2": nota2, "media": (nota1 + nota2) / 2}
for nome, dados in boletim.items():
    situacao = "Aprovado" if dados["media"] >= 7 else "Reprovado"
    print(f"Aluno: {nome}\nNota 1: {dados['nota_1']}\nNota 2: {dados['nota_2']}\nMédia: {dados['media']:.2f}\nSituação: {situacao}")
