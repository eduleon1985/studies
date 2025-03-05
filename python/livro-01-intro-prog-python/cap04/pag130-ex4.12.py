### PT-BR (🇧🇷): 
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação.
# A) para residências
# B) para indústrias
# C) para comércios
# Calcule o preço a pagar de acordo com a tabela abaixo.

### EN (🇺🇸):  
# Write a program that calculates the amount to be paid for electricity supply.  
# Ask for the number of kWh consumed and the type of installation.  
# A) for residences  
# B) for industries  
# C) for businesses  
# Calculate the amount to be paid according to the table below.

### Price by type and consumption range
# Type              # Range             # Price (R$)
# Residences        Up to 500               0,40
#                   Above 500               0,65
# Business          Up to 1000              0,55
#                   Above 1000              0,60
# Industries        Up to 5000              0,55
#                   Above 5000              0,60

print("=" * 10, " INÍCIO ", "=" * 10)
print("A = Residencial")
print("B = Industrial")
print("C = Comercial")

tipo = input("Informe o tipo de instalação: A, B ou C: ")
kwh = int(input("Informe a quantidade de kWh consumida no mês: "))

print("=" * 30)

if tipo == "A":
    if kwh <= 500:
        valor = kwh * 0.4
    else:
        valor = kwh * 0.65
elif tipo == "B":
    if kwh <= 1000:
        valor = kwh * 0.55
    else:
        valor = kwh * 0.60
elif tipo == "C":
    if kwh <= 5000:
        valor = kwh * 0.55
    else:
        valor = kwh * 0.60
else:
    print("Você não está apto a usar um computador!")

print(f"Você consumiu {kwh}kWh e sua conta ficou em R${valor}")

print("=" * 10, "  FIM   ", "=" * 10)