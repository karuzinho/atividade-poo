grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7, 8}

print("União:", grupo_a | grupo_b)
print("Em ambos:", grupo_a & grupo_b)
print("Apenas A:", grupo_a - grupo_b)
print("Apenas B:", grupo_b - grupo_a)
print("Apenas um dos grupos:", grupo_a ^ grupo_b)
