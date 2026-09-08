soma = 0
aceitos = 0

while aceitos < 10:
    codigo = int(input("Código divisível por 3: "))
    if codigo % 3 == 0:
        soma += codigo
        aceitos += 1
    else:
        print("Código ignorado: não é divisível por 3.")

print("Soma dos códigos aceitos:", soma)
