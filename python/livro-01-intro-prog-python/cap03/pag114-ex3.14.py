# PT-BR (🇧🇷): 
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# EN (🇺🇸): 
# Write a program that asks the user for the number of kilometers driven in a rented
# as well as the number of days the car was rented.
# Calculate the total price to be paid, considering that the car costs R$ 60 per day
# and R$ 0.15 per kilometer driven.

print("=== === === === ===")
distancia = float(input("Informe quantos km você percorreu com o carro: "))
periodo = float(input("Quantos dias você ficou com o carro? "))
preco = (periodo * 60) + (distancia * 0.15)
print("...")
print(f"Você ficou com o carro por {periodo} dias, rodou {distancia}km e o valor total a pagar é de R${preco}")
print("=== === === === ===")