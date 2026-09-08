inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

multiplos = [numero for numero in range(min(inicio, fim), max(inicio, fim) + 1) if numero % 7 == 0]
print("Quantidade de múltiplos de 7:", len(multiplos))
