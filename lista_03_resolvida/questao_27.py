contatos = []
while True:
    contatos.append({
        "nome": input("Nome: "),
        "endereco": input("Endereço: "),
        "dd": input("DD: "),
        "telefone": input("Telefone: "),
    })
    if input("Cadastrar outra pessoa? (s/n): ").lower() != "s":
        break
with open("agenda.txt", "w", encoding="utf-8") as arquivo:
    for contato in contatos:
        arquivo.write(f"Nome: {contato['nome']}\nEndereço: {contato['endereco']}\n")
        arquivo.write(f"DD: {contato['dd']}\nTelefone: {contato['telefone']}\n{'-' * 20}\n")

nome = input("Nome para pesquisa: ").lower()
encontrado = next((item for item in contatos if item["nome"].lower() == nome), None)
print(f"DD: {encontrado['dd']} | Telefone: {encontrado['telefone']}" if encontrado else "Contato não encontrado.")
