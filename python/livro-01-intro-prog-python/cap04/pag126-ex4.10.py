### PT-BR (🇧🇷): 
# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.

### EN (🇺🇸):
# Write a program that reads two numbers and asks which operation you want to perform.
# You should be able to calculate addition (+), subtraction (-), multiplication (*), and division (/).
# Display the result of the requested operation. 

x = int(input("Informe um valor inteiro para X: "))
y = int(input("Informe um valor inteiro para Y: "))
print("")
print("a - Soma")
print("b - Subtração")
print("c - Multiplicação")
print("d - Divisão")
operacao = input("Informe a opção desejada (a, b, c ou d): ")
if operacao == "a":
    soma = x + y
    print(f"Soma: x + y = {soma}")
elif operacao == "b":
    diferenca = x - y
    print(f"Subtração: x - y = {diferenca}")
elif operacao == "c":
    produto = x * y
    print(f"Multiplicação: x * y = {produto}")
elif operacao == "d":
    resto = x / y
    print(f"Divisão: x / y = {resto}")
else:
    print("Você é burro bagarai e não consegue seguir uma instrução simples.")