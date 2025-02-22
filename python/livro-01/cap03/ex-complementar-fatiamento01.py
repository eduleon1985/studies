# Exercício de Fatiamento | Slicing Exercise
# 📌 Português:
# Peça ao usuário para digitar um e-mail no formato "usuario@dominio.com".
# Exiba apenas o nome do usuário, removendo o domínio.

email = input("Digite seu e-mail, magnata: ")
usuario = email[:email.index("@")]
print(f"O nome do magnata é {usuario}")