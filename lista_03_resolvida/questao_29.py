import csv

estudantes = []
for numero in range(1, 11):
    nome = input(f"Nome do estudante {numero}: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2
    situacao = "APROVADO" if media >= 6 else "REPROVADO"
    estudantes.append([nome, nota1, nota2, media, situacao])
for estudante in estudantes:
    print(f"{estudante[0]} | {estudante[1]:.1f} | {estudante[2]:.1f} | {estudante[3]:.1f} | {estudante[4]}")

aprovados = sum(estudante[4] == "APROVADO" for estudante in estudantes)
print(f"Aprovados: {aprovados} | Reprovados: {10 - aprovados}")
with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "nota_1", "nota_2", "media", "situacao"])
    escritor.writerows(estudantes)
