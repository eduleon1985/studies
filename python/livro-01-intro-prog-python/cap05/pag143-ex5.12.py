### PT-BR (🇧🇷): 
# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.

### EN (🇺🇸):
# Modify the previous program to also ask for the monthly deposit amount.
# Display the monthly balance for the first 24 months.
# Print the total interest earned during this period.

deposito = float(input("Depósito inicial: R$ "))
juros = float(input("Informe a taxa de juros ao mês (%): "))

n = 1
valor_acumulado = 0

while n <= 24:
    novo_deposito = float(input(f"Informe quanto você está depositando no mês {n}: R$ "))
    valor_acumulado = valor_acumulado + ((deposito * juros/100)) + novo_deposito
    print(f"Mês {n}: o valor atualizado é de R${valor_acumulado:5.2f} e o valor do seu saldo é de {deposito + valor_acumulado:5.2f}")
    n = n + 1