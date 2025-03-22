### PT-BR (🇧🇷): 
# Crie uma lista com nomes de produtos e outra com suas respectivas quantidades em estoque.
# Use a função zip e um for para exibir a seguinte frase para cada par:
# "O produto [nome] tem [quantidade] unidades em estoque."

### EN (🇺🇸):
# Create a list with product names and another with their respective quantities in stock.
# Use the zip function and a for loop to display the following message for each pair:
# "The product [name] has [quantity] units in stock."

produtos = ["Óculos Ray Ban", "iPad", "iPhone", "MacBook Pro"]
quantidade = 50, 20, 35, 10

for i, j in zip(produtos, quantidade):
    print(f"Produto: {i} - Quantidade: {j} unidades")