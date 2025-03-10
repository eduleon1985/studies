### PT-BR (🇧🇷): 
# Escreva um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1.

### EN (🇺🇸):
# Write a program that reads a value and prints the number of banknotes needed to pay that amount.
# To simplify, we will only work with integer values and banknotes of R$ 50, R$ 20, R$ 10, R$ 5, and R$ 1.

valor_a_sacar = int(input("Digite o valor a sacar: "))
cedulas = 0
maiorcedula = 100
valor_a_pagar = valor_a_sacar

while True:
    if maiorcedula <= valor_a_pagar:
        valor_a_pagar -= maiorcedula
        cedulas += 1
    else:
        print(f"{cedulas} cédulas(s) de R${maiorcedula}")
        if valor_a_pagar == 0:
            break

        if maiorcedula == 100:
            maiorcedula = 50
        if maiorcedula == 50:
            maiorcedula = 20
        elif maiorcedula == 20:
            maiorcedula = 10
        elif maiorcedula == 10:
            maiorcedula = 5
        elif maiorcedula == 5:
            maiorcedula = 1
        cedulas = 0