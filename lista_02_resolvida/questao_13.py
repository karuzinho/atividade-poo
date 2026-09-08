disciplina = {"nome": "POO", "professor": "Professor", "carga_horaria": 60, "periodo": "2026.1"}
chave = input("Chave para consultar: ")
print("A chave existe." if chave in disciplina else "A chave não foi encontrada.")
