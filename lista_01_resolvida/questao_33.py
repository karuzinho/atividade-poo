tempos = [float(input(f"Tempo do servidor {numero} (ms): ")) for numero in range(1, 5)]
print(f"Menor tempo: {min(tempos):.2f} ms")
