softwares = ["Windows", "Python", "VS Code", "Chrome", "LibreOffice"]
print("Lista original:", softwares)

novo = input("Novo software: ")
softwares.append(novo)
removido = softwares.pop(1)

print(f"Removido: {removido}")
print("Lista atualizada:", softwares)
