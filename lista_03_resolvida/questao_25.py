matriz = []
for linha in range(4):
    valores = []
    for coluna in range(3):
        valores.append(float(input(f"Valor [{linha}][{coluna}]: ")))
    matriz.append(valores)

valores = [valor for linha in matriz for valor in linha]
print("Existem valores repetidos na matriz." if len(valores) != len(set(valores)) else "Não existem valores repetidos na matriz.")
