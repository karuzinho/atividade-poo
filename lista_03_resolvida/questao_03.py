adequados = 0
lentos = 0
soma = 0
maior = None

for numero in range(1, 11):
    latencia = float(input(f"Latência do teste {numero} (ms): "))
    soma += latencia
    maior = latencia if maior is None or latencia > maior else maior
    if latencia <= 100:
        adequados += 1
    else:
        lentos += 1

print(f"Adequados: {adequados}")
print(f"Com lentidão: {lentos}")
print(f"Média: {soma / 10:.2f} ms")
print(f"Maior latência: {maior:.2f} ms")
