def converter(temperatura, origem, destino):
    if origem == destino:
        return temperatura
    if origem == "C":
        celsius = temperatura
    elif origem == "F":
        celsius = (temperatura - 32) * 5 / 9
    else:
        celsius = temperatura - 273.15

    if destino == "C":
        return celsius
    if destino == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


while True:
    temperatura = float(input("Temperatura: "))
    origem = input("Escala de origem (C/F/K): ").upper()
    destino = input("Escala de destino (C/F/K): ").upper()

    if origem not in "CFK" or destino not in "CFK":
        print("Escala inválida.")
    else:
        print(f"Resultado: {converter(temperatura, origem, destino):.2f} °{destino}")

    if input("Nova conversão? (s/n): ").lower() != "s":
        break
