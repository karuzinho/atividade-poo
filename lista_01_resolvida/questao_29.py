frequencia = float(input("Frequência (%): "))
media = float(input("Média: "))
print("Acesso autorizado." if frequencia >= 75 and media >= 7 else "Acesso negado.")
