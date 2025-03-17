### PT-BR (🇧🇷): 
# Exercício de Listas
# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
# Estou refazendo apenas para me recordra como se faz

### EN (🇺🇸):
# Write a program that reads two lists and generates a third one with the elements of the first two.

# Criação das listas vazias
lista1 = []
lista2 = []
lista3 = []

# Inserindo elementos na lista 1
while True:
    n = int(input("Lista 1 - Digite um  número inteiro qualquer, 0 (zero) para sair: "))
    if n == 0:
        break
    lista1.append(n)

print("*" * 30)

while True:
    n = int(input("Lista 2 - Digite um número inteiro qualquer, 0 (zero) para sair: "))
    if n == 0:
        break
    lista2.append(n)

lista3.extend(lista1)
lista3.extend(lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")



# Inserindo elementos na lista 2