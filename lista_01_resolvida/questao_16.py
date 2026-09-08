tensao = float(input("Tensão (V): "))
corrente = float(input("Corrente (A): "))
if corrente != 0:
    print(f"Resistência: {tensao / corrente:.2f} Ω")
else:
    print("A corrente não pode ser zero.")
