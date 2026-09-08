ano = int(input("Ano: "))
bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)
print("É bissexto." if bissexto else "Não é bissexto.")
