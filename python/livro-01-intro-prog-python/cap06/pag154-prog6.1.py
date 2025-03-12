### PT-BR (🇧🇷): 
# Exercício de Listas
# Crie um programa que calcula a média aritmética

### EN (🇺🇸):
# List Exercise
# Create a program that calculates the arithmetic mean

notas = [6, 5, 7, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1

print(f"Média: {soma / x:5.2f}")