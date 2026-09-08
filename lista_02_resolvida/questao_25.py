def filtrar_intervalo(tempos, limite_inferior, limite_superior):
    """Retorna os valores entre os dois limites, inclusive."""
    return [tempo for tempo in tempos if limite_inferior <= tempo <= limite_superior]

tempos = [15, 22, 35, 48, 60, 78, 90, 120]
print(filtrar_intervalo(tempos, 35, 78))
