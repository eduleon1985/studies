### PT-BR (🇧🇷): 
# Exercício de Listas
# Crie um programa que lê cinco números, armazena-os em uma lista e depois solicita ao usuário que escolha um número a mostrar.
# O objetivo é, por exemplo, ler 12, 15, 5, 2, 8 e armazená-los na lista.
# Depois, se o usuário digitar 2, ele imprimirá o segundo número digitado, 3, o teceiro, e assim sucessivamente.

### EN (🇺🇸):
# List Exercise
# Create a program that reads five numbers, stores them in a list, and then asks the user to choose a number to display.
# The goal is, for example, to read 12, 15, 5, 2, 8 and store them in the list.
# Then, if the user enters 2, the program will print the second number entered, 3 for the third, and so on.

numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Número {x + 1}: "))
    x += 1

while True:
    escolhido = int(input("Informe a posição que deseja imprimir. 0 para sair: "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número {numeros[escolhido - 1]}")