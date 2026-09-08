tensao = float(input("Tensão (V): "))
resistencia = float(input("Resistência (Ω): "))
if resistencia != 0:
    print(f"Corrente: {tensao / resistencia:.2f} A")
else:
    print("A resistência não pode ser zero.")
