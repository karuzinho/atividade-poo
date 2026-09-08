nota = float(input("Nota final: "))
if not 0 <= nota <= 10:
    print("Nota inválida.")
elif nota >= 7:
    print("Aprovado.")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")
