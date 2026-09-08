class Pokemon:
    def __init__(self, numero, nome, tipo, nivel, hp):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp

    def resumo(self):
        return f"#{self.numero} {self.nome} | {self.tipo} | nível {self.nivel} | HP {self.hp}"

    def atualizar(self, tipo, nivel, hp):
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp

def localizar(pokedex, numero):
    return next((pokemon for pokemon in pokedex if pokemon.numero == numero), None)

pokedex = []
while True:
    print("0-Sair | 1-Cadastrar | 2-Consultar | 3-Atualizar | 4-Excluir | 5-Listar")
    opcao = input("Opção: ")
    if opcao == "0":
        break
    if opcao == "1":
        numero = int(input("Número da Pokédex: "))
        if localizar(pokedex, numero):
            print("Número já cadastrado.")
            continue
        pokedex.append(Pokemon(numero, input("Nome: "), input("Tipo: "), int(input("Nível: ")), int(input("HP: "))))
        print("Pokémon cadastrado.")
    elif opcao in {"2", "3", "4"}:
        pokemon = localizar(pokedex, int(input("Número da Pokédex: ")))
        if not pokemon:
            print("Pokémon não encontrado.")
        elif opcao == "2":
            print(pokemon.resumo())
        elif opcao == "3":
            pokemon.atualizar(input("Tipo: "), int(input("Nível: ")), int(input("HP: ")))
            print("Pokémon atualizado.")
        else:
            pokedex.remove(pokemon)
            print("Pokémon excluído.")
    elif opcao == "5":
        if not pokedex:
            print("Pokédex vazia.")
        for pokemon in pokedex:
            print(pokemon.resumo())
    else:
        print("Opção inválida.")
