### PT-BR (🇧🇷): 
# Exercício de Listas
# Crie um programa que calcula a média aritmética
# Desta vez, vamos ler as notas, uma a uma

### EN (🇺🇸):
# List Exercise
# Develop a program that determines the arithmetic average.
# This time, we will read the grades one by one.

notas = [6, 5, 7, 8, 9]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x += 1

x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]:6.2}")
    x += 1

print(f"Média: {soma / x:5.2f}")