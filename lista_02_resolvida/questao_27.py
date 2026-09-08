from pathlib import Path

nome_arquivo = input("Nome do arquivo .txt: ")
arquivo = Path(nome_arquivo)
if not arquivo.exists():
    print("Arquivo não encontrado.")
else:
    ocorrencias = {}
    for caractere in arquivo.read_text(encoding="utf-8").lower():
        if caractere.isalpha():
            ocorrencias[caractere] = ocorrencias.get(caractere, 0) + 1
    for letra in sorted(ocorrencias):
        print(f"{letra}: {ocorrencias[letra]}")
