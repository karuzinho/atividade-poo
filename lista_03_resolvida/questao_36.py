import csv
from pathlib import Path

ARQUIVO = Path("manutencao.csv")

def carregar():
    if not ARQUIVO.exists():
        return []
    with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
        return [{"nome": linha["nome"], "custo": float(linha["custo"])} for linha in csv.DictReader(arquivo)]

def salvar(equipamentos):
    with ARQUIVO.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "custo"])
        escritor.writeheader()
        escritor.writerows(equipamentos)

def listar(equipamentos):
    for indice, equipamento in enumerate(equipamentos):
        print(f"{indice}: {equipamento['nome']} - R$ {equipamento['custo']:.2f}")

def cadastrar(equipamentos):
    equipamentos.append({"nome": input("Nome: "), "custo": float(input("Custo: R$ "))})

def atualizar(equipamentos):
    listar(equipamentos)
    indice = int(input("Índice: "))
    if 0 <= indice < len(equipamentos):
        equipamentos[indice] = {"nome": input("Novo nome: "), "custo": float(input("Novo custo: R$ "))}
    else:
        print("Índice inválido.")

def excluir(equipamentos):
    listar(equipamentos)
    indice = int(input("Índice: "))
    if 0 <= indice < len(equipamentos):
        print("Excluído:", equipamentos.pop(indice)["nome"])
    else:
        print("Índice inválido.")

equipamentos = carregar()
while True:
    print("1-Cadastrar 2-Listar 3-Atualizar 4-Excluir 5-Maior custo 0-Sair")
    opcao = input("Opção: ")
    if opcao == "0":
        salvar(equipamentos)
        break
    if opcao == "1":
        cadastrar(equipamentos)
    elif opcao == "2":
        listar(equipamentos)
    elif opcao == "3":
        atualizar(equipamentos)
    elif opcao == "4":
        excluir(equipamentos)
    elif opcao == "5" and equipamentos:
        maior = max(equipamentos, key=lambda item: item["custo"])
        print(f"Maior custo: {maior['nome']} - R$ {maior['custo']:.2f}")
    else:
        print("Opção inválida ou lista vazia.")
