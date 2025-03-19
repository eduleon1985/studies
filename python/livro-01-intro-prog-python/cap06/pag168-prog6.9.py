### PT-BR (🇧🇷): 
# Tópico: Listas, Pesquisa

### EN (🇺🇸):
# Topic: Lists, Search (checking if an element is in the list or not)

lista = [15, 3, 6, 39, 56, 23, 34, 57, 99, 1, 53, 18, 27, 45, 91, 82, 86, 84, 32, 51, 41, 30, 67, 56, 34, 19, 21, 23, 73, 37, 71, 75, 83, 27, 28]
numero = int(input("Digite um inteiro qualquer para procurar: "))

achou = False
x = 0

while x < len(lista):
    if lista[x] == numero:
        achou = True
        break
    x += 1

if achou:
    print(f"A lista tem {len(lista)} posições.")
    print(f"O número {numero} foi achado na posição {x}")
else:
    print(f"O número {numero} não está na lista")