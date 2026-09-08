def exibir_nome_do_programa():
    """Apresenta o nome do sistema."""
    print("Sistema de Gerenciamento Acadêmico")

def exibir_menu():
    """Exibe as opções disponíveis."""
    print("1-Cadastrar estudante\n2-Listar estudantes\n3-Alterar situação\n0-Sair")

def cadastrar_estudante():
    """Informa que a opção de cadastro foi selecionada."""
    print("Opção Cadastrar estudante selecionada.")

def listar_estudantes():
    """Informa que a opção de listagem foi selecionada."""
    print("Opção Listar estudantes selecionada.")

def alterar_situacao_estudante():
    """Informa que a opção de alteração foi selecionada."""
    print("Opção Alterar situação selecionada.")

def opcao_invalida():
    """Informa que a opção não existe."""
    print("Opção inválida.")

def finalizar_programa():
    """Apresenta a mensagem de encerramento."""
    print("Sistema encerrado.")

def main():
    """Coordena a execução do menu acadêmico."""
    exibir_nome_do_programa()
    exibir_menu()
    opcao = input("Opção: ")
    if opcao == "1":
        cadastrar_estudante()
    elif opcao == "2":
        listar_estudantes()
    elif opcao == "3":
        alterar_situacao_estudante()
    elif opcao == "0":
        finalizar_programa()
    else:
        opcao_invalida()

main()
