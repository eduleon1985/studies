# PT-BR (🇧🇷): 
# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

# EN (🇺🇸): 
# Write a program that calculates the travel time for a car trip.
# Ask for the distance to be traveled and the expected average speed for the trip.

print("===")
distancia = float(input("Quão longe fica o seu destino, magnata? Responda em 'km' (apenas os números): "))
vm = float(input("Quão rápido você pretende ir? Responda, em km/h (apenas os números): "))
tempo_estimado = distancia / vm
print(f"Você vai se deslocar {distancia} km, a uma velocidade média de {vm} km/h, logo, o tempo estimado é de {tempo_estimado}h.")
print("===")