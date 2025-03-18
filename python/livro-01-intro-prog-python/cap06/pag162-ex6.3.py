### PT-BR (🇧🇷): 
# Tópico: Listas
# Faça um programa que leia dupercorra duas listas e que gere uma terceira sem elementos repetidos.

### EN (🇺🇸):
# Topic: Lists
# Write a program that reads and iterates through two lists, generating a third one without duplicate elements.

# git commit -m "Implemented a program to merge two lists without duplicates."

lista1 = []
lista2 = []
lista3 = []

# Lista 1
while True:
    n = int(input("Lista 1: Insira um número inteiro; 0 para sair: "))
    if n == 0:
        break
    lista1.append(n)
print("Fim da Lista 1")

# Lista 2
while True:
    n = int(input("Lista 2: Insira um número inteiro; 0 para sair: "))
    if n == 0:
        break
    lista2.append(n)

i = 0
while i < len(lista1):
    if lista1[i] not in lista3:
        lista3.append(lista1[i])
    i += 1


i = 0
while i < len(lista2):
    if lista2[i] not in lista3:
        lista3.append(lista2[i])
    i += 1

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3, sem repetidos: {lista3}")