nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Média: {media:.2f}")
print("Aprovado." if media >= 6 else "Reprovado.")
