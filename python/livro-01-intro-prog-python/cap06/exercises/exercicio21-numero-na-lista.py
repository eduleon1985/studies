### PT-BR (🇧🇷): 
# Crie uma lista com alguns números inteiros. 
# Depois, peça para o usuário digitar um número e verifique se esse número está na lista. 
# Mostre uma mensagem dizendo se ele está ou não.

### EN (🇺🇸):
# Create a list with some integers. 
# Then, ask the user to enter a number and check if that number is in the list. 
# Print a message indicating whether it was found or not.

numeros = [2, 3, 5, 7, 9, 11, 15, 17, 18, 20, 24, 27, 28, 29, 30, 31, 33, 34, 38, 41, 45, 46, 52, 59, 66, 68, 69, 70, 71, 73, 77, 82, 85, 87, 91, 93, 94, 96, 99]

entrada = int(input("Digite um número: "))

if entrada in numeros:
    print(f"O número {entrada} está na lista!")
else:
    print("Não está na lista.")