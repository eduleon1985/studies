# PT-BR (🇧🇷): 
# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

# EN (🇺🇸): 
# Create a program that asks for the price of a product and the discount percentage.
# Display the discount amount and the final price to pay.

produto = input("Informe o produto: ")
preco = float(input("Informe o preço: "))
desconto = float(input("Informe o percentual de desconto: "))
valor_com_desconto = preco - ((preco * desconto) / 100)
print(f"O produto {produto} tem o preço original de $ {preco}, você ganhou um desconto de {desconto}% e o valor com desconto é de {valor_com_desconto}.")

