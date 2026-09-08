curso1 = int(input("Quantidade de alunos do curso 1: "))
curso2 = int(input("Quantidade de alunos do curso 2: "))
if curso1 > curso2:
    mensagem = "O Curso 1 possui mais alunos."
elif curso2 > curso1:
    mensagem = "O Curso 2 possui mais alunos."
else:
    mensagem = "Os dois cursos possuem a mesma quantidade de alunos."
print(mensagem)
with open("resultado_cursos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(mensagem)
