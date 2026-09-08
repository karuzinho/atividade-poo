def calcular(valor1, valor2):
    produto = valor1 * valor2
    return produto if produto <= 1000 else valor1 + valor2


a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
print("Resultado:", calcular(a, b))
