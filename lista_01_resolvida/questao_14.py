preco = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
desconto = float(input("Desconto: R$ "))
print(f"Total a pagar: R$ {preco * quantidade - desconto:.2f}")
