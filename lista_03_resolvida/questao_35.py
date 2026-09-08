equipamentos = []
while True:
    print("1-Cadastrar | 2-Listar | 3-Atualizar | 4-Excluir | 5-Maior custo | 0-Sair")
    opcao = input("Opção: ")
    if opcao == "0":
        break
    if opcao == "1":
        equipamentos.append({"nome": input("Nome: "), "custo": float(input("Custo: R$ "))})
    elif opcao == "2":
        for indice, item in enumerate(equipamentos):
            print(f"{indice}: {item['nome']} - R$ {item['custo']:.2f}")
    elif opcao in {"3", "4"}:
        indice = int(input("Índice do equipamento: "))
        if 0 <= indice < len(equipamentos):
            if opcao == "3":
                equipamentos[indice] = {"nome": input("Novo nome: "), "custo": float(input("Novo custo: R$ "))}
            else:
                equipamentos.pop(indice)
        else:
            print("Índice inválido.")
    elif opcao == "5" and equipamentos:
        maior = max(equipamentos, key=lambda item: item["custo"])
        print(f"Maior custo: {maior['nome']} - R$ {maior['custo']:.2f}")
    else:
        print("Opção inválida ou lista vazia.")
