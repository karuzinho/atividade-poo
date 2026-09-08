convidados = ["Ana", "Bruno", "Carla", "Diego", "Eva"]
for nome in convidados:
    print(f"{nome}, você está convidado para o jantar.")

indice = convidados.index(input("Quem não poderá comparecer? "))
convidados[indice] = input("Nome do substituto: ")
convidados.insert(0, input("Novo convidado para o início: "))
convidados.insert(len(convidados) // 2, input("Novo convidado para o meio: "))
convidados.append(input("Novo convidado para o final: "))
while len(convidados) > 2:
    removido = convidados.pop()
    print(f"Desculpe, {removido}, a mesa ficou menor.")
for nome in convidados:
    print(f"{nome}, você continua convidado.")
convidados.clear()
print("Lista final:", convidados)
