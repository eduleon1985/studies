### PT-BR (🇧🇷): 
# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

### EN (🇺🇸):
# Write a program that asks for the initial debt amount and the monthly interest rate.
# Also, ask for the monthly payment amount.
# Print the number of months required to pay off the debt, the total amount paid, and the total interest paid.

divida = float(input("Qual o valor inicial da dívida? R$ "))
taxa = float(input("Digite a taxa de jurso (%): ")) / 100 # Valor convertido para decimal
pagamento_mensal = int(input("Quanto você vai pagar por mês? R$ "))

saldo = divida
meses = 0
total_juros = 0
total_pago = 0

# Verifica se a dívida é possível de ser paga
if pagamento_mensal <= saldo * taxa:
    print("O pagamento é insuficiente para cobrir os juros. A dívida nunca será quitada deste jeito.")
else:
    # Loop para calcular o pagamento da dívida
    while saldo > 0:
        # Calcula os juros do mês
        juros_mes = saldo * taxa
        saldo += juros_mes # Adiciona os juros ao saldo

        # Atualiza o total de juros pagos
        total_juros += juros_mes
        
        # Realiza o pagamento mensal
        saldo -= pagamento_mensal
    
        # Garante que o saldo nunca seja negativo
        if saldo < 0:
            saldo = 0

        # Atualiza o total pago e o contador de meses
        total_pago += pagamento_mensal
        meses += 1

    # Exibe os resultados
    print(f"A dívida foi quitada em {meses} meses.")
    print(f"Total pago: R$ {total_pago:5.2f}")
    print(f"Total de juros pagos: R$ {total_juros:.2f}")