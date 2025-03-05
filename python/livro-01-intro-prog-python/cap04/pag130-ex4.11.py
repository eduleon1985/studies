### PT-BR (🇧🇷): 
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

### EN (🇺🇸):
# Write a program to approve a bank loan for purchasing a house.
# The program should ask for the house price, the salary, and the number of years to pay.
# The monthly installment cannot exceed 30% of the salary.
# Calculate the installment amount as the house price divided by the number of months to pay.

# Entrada:
# 1 - Valor da casa
# 2 - Salário
# 3 - Anos a pagar

# Regras:
# 1 - O valor da prestação não pode ultrapassar 30% do salário

print("===")

# Entrada de dados
valor_casa = float(input("Informe o valor do imóvel desejado: "))
salario = float(input("Informe seu salário: R$ "))
anos = int(input("Em quantos anos pretende pagar o imóvel? "))

# Cálculo da quantidade de parcelas
meses = anos * 12

# Cálculo do valor da parcela
valor_parcela = valor_casa / meses

print("===")

if valor_parcela > ((salario * 30) / 100):
    print("Infelizmente o valor da parcela ultrapassa 30% da sua renda")
else:
    print(f"O valor do imóvel que você deseja é de R${valor_casa}")
    print(f"Você pretende pagar em {meses} parcelas")
    print(f"O valor da parcela é de R${valor_parcela}")

print("===")