x = float(input("Coordenada x: "))
y = float(input("Coordenada y: "))
if x > 0 and y > 0:
    print("Primeiro quadrante.")
elif x < 0 and y > 0:
    print("Segundo quadrante.")
elif x < 0 and y < 0:
    print("Terceiro quadrante.")
elif x > 0 and y < 0:
    print("Quarto quadrante.")
else:
    print("O ponto está em um dos eixos ou na origem.")
