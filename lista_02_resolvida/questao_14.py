frase = input("Frase: ").lower()
ocorrencias = {}
for palavra in frase.split():
    ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1
for palavra, quantidade in ocorrencias.items():
    print(f"{palavra}: {quantidade}")
