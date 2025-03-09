### PT-BR (🇧🇷): 
# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

### EN (🇺🇸):
# Write a program that reads integer numbers from the keyboard.
# The program should keep reading numbers until the user enters 0 (zero).
# At the end of execution, display the total count of numbers entered, as well as the sum and the arithmetic mean.

s = 0
soma = 0
media = 0

while True:
    x = int(input("Digite um valor qualquer, e 0 (zero) para sair: "))
    if x == 0:
        break
    soma += x
    s += 1

media = soma / s

print(f"Você digitou {s} números.")
print(f"A soma dos números é {soma} e a média aritmética é {media}")