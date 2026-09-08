ocorrencias = {}
for numero in range(1, 11):
    codigo = int(input(f"Código {numero}: "))
    ocorrencias[codigo] = ocorrencias.get(codigo, 0) + 1
for codigo, quantidade in sorted(ocorrencias.items()):
    print(f"Código {codigo}: {quantidade} ocorrência(s)")
