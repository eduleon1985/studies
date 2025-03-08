### PT-BR (🇧🇷): 
# Crie um programa que leia dois números e imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas o operador "+"
# Ex: 4 x 5 = 4 + 4 + 4 + 4 + 4 ou 5 + 5 + 5 + 5

### EN (🇺🇸):
# Create a program that reads two numbers and prints the result of multiplying the first by the second.
# Use only the "+" and "-" operators.
# Example: 4 x 5 = 4 + 4 + 4 + 4 + 4 or 5 + 5 + 5 + 5

print("Exercício de multiplicação utilizando operadores de Adição e Subtração.")
print("Escreva apenas valores inteiros e positivos diferente de zero.")

# Solicita ao usuário dos números
x = int(input("Informe um valor para X: "))
y = int(input("Informe um valor para Y: "))

# Inicializa o resultado
resultado = 0
contador = 0

# Cria a string para armazenar a soma repetida
soma_repetida = ""

while contador < y:
    resultado = resultado + x
    soma_repetida += f"{x} + " if contador < y -1 else f"{x}"
    contador = contador + 1

print(f"O resultado de {x} x {y} = {resultado} ou então {soma_repetida}")

