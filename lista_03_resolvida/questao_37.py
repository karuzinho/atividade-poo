import json
from pathlib import Path

ARQUIVO = Path("pokemons.json")

class Pokemon:
    def __init__(self, nome, nivel, tipo="Normal", hp=100, treinador="Ash"):
        self.nome = nome
        self.nivel = nivel
        self.tipo = tipo
        self.hp = hp
        self.treinador = treinador

    def exibir(self):
        return f"{self.nome} | nível {self.nivel} | {self.tipo} | HP {self.hp} | {self.treinador}"

    def atualizar(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def para_dicionario(self):
        return self.__dict__

def carregar():
    if not ARQUIVO.exists():
        return []
    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return [Pokemon(**item) for item in dados]

def salvar(equipe):
    ARQUIVO.write_text(json.dumps([pokemon.para_dicionario() for pokemon in equipe], ensure_ascii=False, indent=2), encoding="utf-8")

equipe = carregar()
while True:
    print("1-Cadastrar 2-Listar 3-Atualizar 4-Excluir 5-Maior nível 0-Sair")
    opcao = input("Opção: ")
    if opcao == "0":
        salvar(equipe)
        break
    if opcao == "1":
        equipe.append(Pokemon(input("Nome: "), int(input("Nível: ")), input("Tipo: "), int(input("HP: ")), input("Treinador: ")))
    elif opcao == "2":
        for pokemon in equipe:
            print(pokemon.exibir())
    elif opcao in {"3", "4"}:
        nome = input("Nome do Pokémon: ").lower()
        pokemon = next((item for item in equipe if item.nome.lower() == nome), None)
        if not pokemon:
            print("Pokémon não encontrado.")
        elif opcao == "3":
            pokemon.atualizar(input("Novo nome: "), int(input("Novo nível: ")))
        else:
            equipe.remove(pokemon)
    elif opcao == "5" and equipe:
        print("Maior nível:", max(equipe, key=lambda item: item.nivel).exibir())
    else:
        print("Opção inválida ou equipe vazia.")
