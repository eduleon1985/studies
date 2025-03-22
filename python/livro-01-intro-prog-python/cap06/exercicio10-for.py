### PT-BR (🇧🇷): 
# Crie uma lista com nomes de produtos, o preço e outra com suas respectivas quantidades em estoque.
# Use a função zip e um for para exibir a seguinte frase para cada par:
# "O produto [nome] tem [quantidade] unidades em estoque e cada um custa [preco]."

### EN (🇺🇸):
# Create a list with product names, price and another with their respective quantities in stock.
# Use the zip function and a for loop to display the following message for each pair:
# "The product [name] has [quantity] units in stock and it costs [price] each."

produto = ["iPad", "iPhone", "MacBook"]
preco = 10.000, 15.000, 12.000
quantidade = 30, 100, 12

for i, j, k in zip(produto, preco, quantidade):
    print(f"O produto {i} custa R${j} e possui {k} unidades em estoque.")