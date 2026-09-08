notas = []
while True:
    entrada = input("Nota (enter para finalizar): ")
    if not entrada:
        break
    notas.append(float(entrada))
try:
    print(f"Média: {sum(notas) / len(notas):.2f}")
except ZeroDivisionError:
    print("A lista está vazia.")
