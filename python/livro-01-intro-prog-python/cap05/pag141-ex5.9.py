### PT-BR (🇧🇷): 
'''
Escreva um programa que leia dois números.
Imprima a divisão inteira do primeiro pelo segundo, assom como o resto da divisão.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
Logo, 40/4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
'''

### EN (🇺🇸):
''' 
Write a program that reads two numbers.
Print the integer division of the first number by the second, as well as the remainder of the division.
Use only the addition and subtraction operators to calculate the result.
Remember that we can understand the quotient of a division as the number of times we can subtract the divisor from the dividend.
For example, 40 ÷ 4 = 10, since we can subtract 4 ten times from 40.
'''

x_dividendo = int(input("X: "))
y_divisor = int(input("Y: "))

quociente = 0
resto = x_dividendo

while resto >= y_divisor:
    resto -= y_divisor
    quociente += 1

print(f"O quociente da divisão é {quociente} e o resto é {resto}.")