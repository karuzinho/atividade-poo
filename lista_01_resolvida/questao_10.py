valor = float(input("Valor financiado: R$ "))
taxa = float(input("Taxa mensal (%): ")) / 100
meses = int(input("Quantidade de meses: "))
juros = valor * taxa * meses
print(f"Juros: R$ {juros:.2f}")
print(f"Montante: R$ {valor + juros:.2f}")
