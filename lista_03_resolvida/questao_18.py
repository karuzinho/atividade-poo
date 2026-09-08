equipamentos = []

for numero in range(1, 6):
    nome = input(f"Nome do equipamento {numero}: ")
    preco = float(input("Preço: R$ "))
    equipamentos.append({"nome": nome, "preco": preco})

for equipamento in equipamentos:
    print(f"{equipamento['nome']}: R$ {equipamento['preco']:.2f}")

mais_caro = max(equipamentos, key=lambda equipamento: equipamento["preco"])
print(f"Mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")
