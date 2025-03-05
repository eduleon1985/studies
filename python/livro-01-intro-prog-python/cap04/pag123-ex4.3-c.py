# PT-BR (🇧🇷): 
# Escreva um programa que leia três números e que imprima o maior e o menor.

# EN (🇺🇸): 
# "Write a program that reads three numbers and prints the largest and the smallest."

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

maior = max(a, b, c)
menor = min(a, b, c)

print(f"O maior valor é {maior}, e o menor valor é {menor}")