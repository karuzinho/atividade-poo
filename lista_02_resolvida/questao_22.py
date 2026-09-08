def cadastrar_estudante():
    """Solicita os dados do estudante e confirma o cadastro."""
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    print(f"Cadastro realizado: {nome} | {matricula} | {curso}")

cadastrar_estudante()
