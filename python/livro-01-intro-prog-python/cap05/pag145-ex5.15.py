### PT-BR (🇧🇷): 
# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos para obter o preço de cada produto.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro "Código inválido"

### EN (🇺🇸):
# Write a program to control a small cash register.
# You should ask the user to enter the product code and the quantity purchased.
# Use the code table to get the price of each product.

'''
CODE        PRICE
1           0.5
2           1.0
3           4.0
5           7.0
9           8.0
'''

quantidade = 0
valor_total = 0

while True:
    codigo = int(input("Digite o código do produto desejado, e Zero para sair: "))
    if codigo == 0:
        break
    elif codigo == 1:
        quantidade =  int(input("Informe a quantidade desejada: "))
        valor_total += quantidade * 0.5
    elif codigo == 2:
        quantidade = int(input("Informe a quantidade desejada: "))
        valor_total+= quantidade * 1
    elif codigo == 3:
        quantidade = int(input("Informe a quantidade desejada: "))
        valor_total += quantidade * 4
    elif codigo == 5:
        quantidade = int(input("Informe a quantidade desejada: "))
        valor_total += quantidade * 7
    elif codigo == 9:
        quantidade = int(input("Informe a quantidade desejada: "))
        valor_total += quantidade * 8
    else:
        int(input("Código inválido, tente novamente: "))

print(f"O valor total da sua compra é de {valor_total}")