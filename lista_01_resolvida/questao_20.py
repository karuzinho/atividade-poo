from datetime import date

nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - ano_nascimento
situacao = "Pode entrar desacompanhado." if idade >= 18 else "Precisa estar acompanhado."
print(f"{nome}, {idade} anos. {situacao}")
