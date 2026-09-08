import csv

equipamentos = []
while True:
    equipamentos.append({"nome": input("Nome do equipamento: "), "custo": float(input("Custo estimado: R$ "))})
    if input("Cadastrar outro? (s/n): ").lower() != "s":
        break
for equipamento in equipamentos:
    print(f"{equipamento['nome']}: R$ {equipamento['custo']:.2f}")

mais_caro = max(equipamentos, key=lambda item: item["custo"])
print(f"Maior custo: {mais_caro['nome']} - R$ {mais_caro['custo']:.2f}")
with open("manutencao.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "custo"])
    escritor.writeheader()
    escritor.writerows(equipamentos)
