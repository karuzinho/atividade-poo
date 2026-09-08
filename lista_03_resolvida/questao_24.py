import csv

estudantes = []
for numero in range(1, 11):
    nome = input(f"Nome do estudante {numero}: ")
    notas = [float(input(f"Nota {avaliacao}: ")) for avaliacao in range(1, 4)]
    media = (notas[0] * 3 + notas[1] * 4 + notas[2] * 3) / 10
    estudantes.append({"nome": nome, "notas": notas, "media": media})
for estudante in estudantes:
    print(f"{estudante['nome']}: {estudante['notas']} | média {estudante['media']:.2f}")

melhor = max(estudantes, key=lambda estudante: estudante["media"])
print(f"Maior média: {melhor['nome']} ({melhor['media']:.2f})")
with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "nota_1", "nota_2", "nota_3", "media"])
    for estudante in estudantes:
        escritor.writerow([estudante["nome"], *estudante["notas"], estudante["media"]])
