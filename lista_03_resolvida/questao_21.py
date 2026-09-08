gabarito = []
respostas = []
for numero in range(1, 26):
    gabarito.append(input(f"Gabarito da questão {numero} (A-E): ").strip().upper())
for numero in range(1, 26):
    respostas.append(input(f"Resposta do estudante na questão {numero} (A-E): ").strip().upper())

acertos = sum(correta == resposta for correta, resposta in zip(gabarito, respostas))
print(f"Acertos: {acertos}")
print(f"Erros: {25 - acertos}")
print(f"Aproveitamento: {acertos / 25 * 100:.1f}%")
