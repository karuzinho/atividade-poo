cavaleiros = ["Aiolia", "Shaka", "Mu", "Milo", "Camus"]
print("Quantidade inicial:", len(cavaleiros))

cavaleiros.append("Aiolos")
cavaleiros.insert(0, "Dohko")
cavaleiros.remove("Milo")
removido = cavaleiros.pop()
print("Último removido:", removido)
print("Primeiro da lista:", cavaleiros[0])

cavaleiros.sort()
for cavaleiro in cavaleiros:
    print(cavaleiro)
print("Quantidade final:", len(cavaleiros))
