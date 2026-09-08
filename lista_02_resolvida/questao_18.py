inventario = {}
for numero in range(1, 4):
    patrimonio = input(f"Patrimônio {numero}: ")
    inventario[patrimonio] = {
        "equipamento": input("Equipamento: "),
        "marca": input("Marca: "),
        "situacao": input("Situação: "),
    }
for patrimonio, dados in inventario.items():
    print(patrimonio, dados)
