vogais = 0
consoantes = 0

for numero in range(1, 11):
    letra = input(f"Letra {numero}: ").strip().lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida.")
    elif letra in "aeiou":
        vogais += 1
    else:
        consoantes += 1

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
