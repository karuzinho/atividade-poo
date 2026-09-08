medicoes = []
for numero in range(1, 6):
    medicoes.append(float(input(f"Medição {numero}: ")))

print("Soma das medições:", sum(medicoes))
