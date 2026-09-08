menor = None
for numero in range(1, 11):
    latencia = float(input(f"Latência {numero} (ms): "))
    menor = latencia if menor is None or latencia < menor else menor

print(f"Menor latência: {menor:.2f} ms")
