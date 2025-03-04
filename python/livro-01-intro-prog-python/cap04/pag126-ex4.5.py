### PT-BR (🇧🇷): 
# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km,
# e R$ 0,45 para viagens mais longas.


### EN (🇺🇸):
# Write a program that asks for the distance a passenger wants to travel in km.
# Calculate the ticket price, charging R$ 0.50 per km for trips up to 200 km,
# and R$ 0.45 for longer trips.

distancia = float(input("Informe a distância a ser percorrida: "))
if distancia <= 200:
    ticket = distancia * 0.5
else:
    ticket = distancia * 0.45

print(f"Distância: {distancia}, valor: R${ticket}")