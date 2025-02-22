# Extraindo o código do produto
# 📌 Português:
# Peça ao usuário um código de produto no formato "ABC-1234" e exiba apenas a parte numérica.

codigo = input("Qual o código do produto? Manda a boa aí, chefe: ")
numeros = codigo[codigo.index("-") + 1 :]
print(f"Os números do código {codigo} são {numeros}")

