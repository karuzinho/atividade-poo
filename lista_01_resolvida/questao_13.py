temperaturas = [float(input(f"Temperatura do sensor {numero}: ")) for numero in range(1, 4)]
print(f"Temperatura média: {sum(temperaturas) / 3:.2f}")
