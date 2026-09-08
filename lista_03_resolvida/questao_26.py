import json

equipamentos = []
while len(equipamentos) < 100:
    equipamentos.append({
        "patrimonio": input("Patrimônio: "),
        "modelo": input("Modelo: "),
        "ano": input("Ano de fabricação: "),
        "situacao": input("Situação: ").upper(),
        "setor": input("Setor: "),
    })
    if input("Cadastrar outro? (s/n): ").lower() != "s":
        break

print("Equipamentos cadastrados:")
for equipamento in equipamentos:
    print(equipamento)

situacao = input("Situação para pesquisa: ").upper()
encontrados = [item for item in equipamentos if item["situacao"] == situacao]
print(f"Encontrados: {len(encontrados)}")
for equipamento in encontrados:
    print(equipamento)
with open("equipamentos.json", "w", encoding="utf-8") as arquivo:
    json.dump(equipamentos, arquivo, ensure_ascii=False, indent=2)

