a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
operacao = input("Operação (+, -, *, /): ")
if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/" and b != 0:
    resultado = a / b
else:
    print("Operação inválida ou divisão por zero.")
    resultado = None
if resultado is not None:
    print("Resultado:", resultado)
