lados = [float(input(f"Lado {numero}: ")) for numero in range(1, 4)]
a, b, c = lados
if a + b > c and a + c > b and b + c > a:
    print("Os valores formam um triângulo.")
    if a == b == c:
        print("Triângulo equilátero.")
    elif a != b and a != c and b != c:
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("Os valores não formam um triângulo.")
