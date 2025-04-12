# PT-BR:
# Peça ao usuário para digitar 10 números inteiros e armazene-os em uma lista.
# Depois, pergunte ao usuário qual número ele deseja buscar, e informe quantas vezes esse número aparece na lista.

# EN:
# Ask the user to enter 10 integers and store them in a list. 
# Then, ask the user for a number to search and display how many times it appears in the list.

numeros = []

for i in range(10):
    n = int(input(f"Digite o {i}º número: "))
    numeros.append(n)

busca = int(input("Informe o número você quer buscar: "))
quantidade = numeros.count(busca)

print(f"O número {busca} aparece {quantidade} vezes na lista.")