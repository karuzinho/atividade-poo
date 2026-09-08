agenda = {}
for numero in range(1, 4):
    nome = input(f"Nome do contato {numero}: ")
    agenda[nome] = input("Telefone: ")
nome = input("Contato para consultar: ")
print(agenda.get(nome, "Contato não encontrado."))
