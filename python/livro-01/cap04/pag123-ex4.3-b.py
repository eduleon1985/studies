# PT-BR (🇧🇷): 
# Escreva um programa que leia três números e que imprima o maior e o menor.

# EN (🇺🇸): 
# "Write a program that reads three numbers and prints the largest and the smallest."

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

menor = a
maior = a

# Verifica o maior número
if (b > maior):
    maior = b
if (c > maior):
    maior = c

# Verifica o menor número
if (b < menor):
    menor = b
if (c < menor):
    menor = c

print(f"Maior = {maior}, menor = {menor}")