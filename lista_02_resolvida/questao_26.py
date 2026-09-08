def calcular_comissao(valor_servico):
    """Calcula 10% do valor de um serviço."""
    return valor_servico * 0.10

valor = float(input("Valor do serviço: R$ "))
print(f"Comissão: R$ {calcular_comissao(valor):.2f}")
