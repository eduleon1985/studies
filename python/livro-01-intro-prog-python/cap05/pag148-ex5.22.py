### PT-BR (🇧🇷): 
# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.

### EN (🇺🇸):
# Write a program that displays a menu with options: addition, subtraction, division, multiplication, and exit.
# Print the multiplication table of the selected operation.
# Repeat until the exit option is chosen.

while True:
    # MENU
    print("*" * 50)
    print("A) Adição")
    print("B) Subtração")
    print("C) Multiplicação")
    print("D) Divisão")
    print("E) Sair")
    
    # Usuário escolhe
    opcao = input("Escolha uma opção do menu acima: ")
    
    # Encerra o programa
    if opcao == "E" or opcao == "e":
        break
    
    # Usuário escolhe dois números
    x = int(input("Informe um valor para x: "))
    y = int(input("Informe um valor para y: "))

    # Executa as operações desejadas
    if opcao == "A" or opcao == "a":
        print("Adição")
        print(f"{x} + {y} = {x + y}")
    elif opcao == "B" or opcao == "b":
        print("Subtração")
        print(f"{x} - {y} = {x - y}")
    elif opcao == "C" or opcao == "c":
        print("Multiplicação")
        print(f"{x} * {y} = {x * y}")
    elif opcao == "D" or opcao == "d":
        print("Divisão")
        print(f"{x} / {y} = {x / y}")