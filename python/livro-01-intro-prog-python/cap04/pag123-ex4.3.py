# PT-BR (🇧🇷): 
# Escreva um programa que leia três números e que imprima o maior e o menor.

# EN (🇺🇸): 
# "Write a program that reads three numbers and prints the largest and the smallest."

print("===")
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

if (a > b) and (a > c):
    maior = a

if (b > a) and (b > c):
    maior = b

if (c > a) and (c > b):
    maior = c

if (a < b) and (a < c):
    menor = a

if (b < a) and (b < c):
    menor = b

if (c < a) and (c < b):
    menor = c

print(f"O maior número é o {maior} e o menor é o {menor}.")
print("===")