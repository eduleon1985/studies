# 5 - Ocultando parte de um CPF | Hiding part of a CPF number
# 📌 Português:
# Peça um CPF no formato "123.456.789-00" e exiba apenas os últimos 4 caracteres, ocultando o restante com *.
# Exemplo de saída:

# 📌 English:
# Ask for a CPF number in the format "123.456.789-00" and display only the last 4 characters, hiding the rest with *.

cpf = input("Insira seu CPF - no formato 123.456.789.00: ")
cpf_oculto = "***.***.***" + cpf[-4:]
print(f"CPF oculto: {cpf_oculto}")