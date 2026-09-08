numero = int(input("Número inteiro não negativo: "))

if numero < 0:
    print("Valor inválido.")
else:
    fatorial = 1
    for valor in range(2, numero + 1):
        fatorial *= valor
    print(f"{numero}! = {fatorial}")
