lista_compras = [
    ["Arroz", 2, 5.49],
    ["Feijão", 3, 3.27],
    ["Azeite", 1, 9.81],
    ["Leite", 4, 1.18],
    ["Manteiga", 5, 3.96]
]

total_geral = 0

for i in lista_compras:
    nome = i[0]
    qtd = i[1]
    preco = i[2]
    total = qtd * preco
    total_geral += total
    print(f"{nome} x {qtd} = R${total:.2f}")

print(f"Total geral: R${total_geral:.2f}")