from pathlib import Path

arquivo = Path("agenda.txt")
if not arquivo.exists():
    print("Execute primeiro a questão 27 para criar agenda.txt.")
else:
    dd_pesquisado = input("DD para pesquisa: ").strip()
    contatos = [bloco for bloco in arquivo.read_text(encoding="utf-8").split("-" * 20) if bloco.strip()]
    encontrados = [bloco for bloco in contatos if f"DD: {dd_pesquisado}" in bloco]
    print(f"Pessoas encontradas: {len(encontrados)}")
    for contato in encontrados:
        print(next(linha for linha in contato.splitlines() if linha.startswith("Nome:")))
