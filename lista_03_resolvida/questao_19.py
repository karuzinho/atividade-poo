valores = []
for numero in range(1, 8):
    valores.append(int(input(f"Valor {numero}: ")))

print("Ordem inversa:", valores[::-1])
