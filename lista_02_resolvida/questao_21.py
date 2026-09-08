programacao = float(input("Horas de Programação: "))
banco = float(input("Horas de Banco de Dados: "))
redes = float(input("Horas de Redes: "))
if programacao < 0 or banco < 0 or redes < 0:
    print("Valores inválidos.")
else:
    print(f"Carga horária total: {programacao + banco + redes:g} horas")
