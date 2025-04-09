# PT-BR:
# Peça ao usuário para digitar 5 números inteiros (um por vez) e armazene esses valores em uma lista. 
# Em seguida, calcule e exiba a soma apenas dos números positivos.

# EN:
# Ask the user to enter 5 integer numbers (one at a time) and store them in a list. 
# Then, calculate and display the sum of only the positive numbers.

numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

soma_positivos = 0

for num in numeros:
    if num > 0:
        soma_positivos += num

print(f"A soma dos números positivos é {soma_positivos} e os números digitados são {numeros}.")



