soma = 0
aceitos = 0
while aceitos < 10:
    valor = int(input("Número divisível por 6: "))
    if valor % 6 == 0:
        soma += valor
        aceitos += 1
    else:
        print("Valor não aceito.")
print("Soma:", soma)
