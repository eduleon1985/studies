# PT-BR:
# Peça ao usuário para digitar 7 números inteiros e armazene-os em uma lista. Depois, exiba:
# - todos os números digitados
# - o maior número
# - o menor número

# EN:
# Ask the user to enter 7 integers and store them in a list. Then, display:
# - all the numbers
# - the largest number
# - the smallest number

lista = []

for i in range(7):
    n = int(input(f"Digite o {i + 1} número inteiro qualquer: "))
    lista.append(n)

print(f"Números digitados: ", lista)
print(f"Maior número: ", max(lista))
print(f"Menor número: ", min(lista))