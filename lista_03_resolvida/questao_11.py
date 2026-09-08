maior = None
for numero in range(1, 16):
    uso = float(input(f"Uso do processador no período {numero}: "))
    maior = uso if maior is None or uso > maior else maior

print(f"Maior valor observado: {maior}")
