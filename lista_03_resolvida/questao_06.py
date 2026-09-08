inicio = int(input("Primeiro número: "))
fim = int(input("Segundo número: "))

for numero in range(min(inicio, fim), max(inicio, fim) + 1):
    print(numero)
