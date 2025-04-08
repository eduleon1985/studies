# PT-BR:
# Peça ao usuário para digitar nomes, um por vez, e adicione cada nome a uma lista. 
# O processo deve continuar até que o usuário digite a palavra "sair". 
# Ao final, exiba todos os nomes digitados.

# EN:
# Ask the user to enter names one by one, adding each to a list. 
# The process should continue until the user types "sair" (which means "exit" in Portuguese). 
# At the end, print all the entered names.

nomes = []

while True:
    nome = input("Digite um nome (sair para encerrar): ")
    if nome == "sair":
        break
    nomes.append(nome)

print(nomes)