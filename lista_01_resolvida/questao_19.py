potencia = float(input("Potência (W): "))
tensao = float(input("Tensão (V): "))
if tensao != 0:
    print(f"Corrente aproximada: {potencia / tensao:.2f} A")
else:
    print("A tensão não pode ser zero.")
