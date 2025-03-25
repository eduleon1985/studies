### PT-BR (🇧🇷): 
# Crie um programa que peça ao usuário para digitar 5 números e os armazene em uma lista.
# Depois, use um for para exibir os números digitados, um por linha.

### EN (🇺🇸):
# Create a program that asks the user to enter 5 numbers and stores them in a list.  
# Then, use a for loop to display the entered numbers, one per line.

numeros = []

x = 5
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

print("Números digitados:") 

for i in numeros:
    print(f"Os números digitados foram: {i}")