# PT-BR:
# Peça ao usuário para digitar um número inteiro. 
# Em seguida, use um laço for para exibir a tabuada desse número de 1 a 10.

# EN:
# Ask the user to enter an integer number. 
# Then, use a for loop to display the multiplication table for that number from 1 to 10.

numero = int(input("Digite um número inteiro qualquer: "))

for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")