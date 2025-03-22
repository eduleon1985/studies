### PT-BR (🇧🇷): 
# Crie uma lista com 5 produtos e outra lista com os respectivos preços.
# Use um laço for para exibir os produtos e seus preços formatados como:
# "Produto: [nome] - Preço: R$ [valor]"


### EN (🇺🇸):
# Create a list with 5 products and another list with their respective prices.
# Use a for loop to display each product and its price formatted as:
# "Product: [name] - Price: $[value]"

produtos = ["Banana", "Tomate", "Alface", "Quiabo", "Melancia"]
precos = [4.99, 7.99, 6.99, 10, 5.99]

for i, j in zip(produtos, precos):
    print(f"Produto: {i}, Preço: R${j}")