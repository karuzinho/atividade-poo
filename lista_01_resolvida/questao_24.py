validos = []
for numero in range(1, 6):
    valor = float(input(f"Medição {numero}: "))
    if 0 < valor < 1000:
        validos.append(valor)
if validos:
    print(f"Média das medições válidas: {sum(validos) / len(validos):.2f}")
else:
    print("Nenhuma medição válida foi informada.")
