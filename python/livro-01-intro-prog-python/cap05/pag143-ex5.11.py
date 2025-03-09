### PT-BR (🇧🇷): 
# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

### EN (🇺🇸):
# Write a program that asks for the initial deposit and the interest rate of a savings account.
# Display the monthly balance for the first 24 months.
# Print the total interest earned during this period.

deposito = float(input("Depósito inicial: R$ "))
juros = float(input("Informe a taxa de jursos: "))

n = 1
valor_acumulado = 0

while n <= 24:
    valor_acumulado = valor_acumulado + ((deposito * juros/100))
    n = n + 1
    print(f"Mês {n}: o valor atualizdo é de R${valor_acumulado} e o valor do seu saldo é de {deposito + valor_acumulado:5.2f}")
