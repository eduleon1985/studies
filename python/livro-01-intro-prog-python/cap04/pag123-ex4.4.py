# PT-BR (🇧🇷): 
# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.

# EN (🇺🇸): 
# Write a program that asks for the employee's salary and calculates the salary increase.
# For salaries above R$ 1,250, apply a 10% increase.
# For salaries equal to or below this amount, apply a 15% increase.

salario = float(input("Seu salário: "))

if salario > 1500:
    aumento = salario + salario * 0.1

if salario <= 1500:
    aumento = salario + salario * 0.15

print(f"Salário inicial: {salario}, aumento: {aumento}")