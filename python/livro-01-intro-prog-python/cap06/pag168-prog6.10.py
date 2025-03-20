### PT-BR (🇧🇷): 
# Tópico: Listas, Pesquisa utilizando a estrutura "for"

### EN (🇺🇸):
# Topic: Lists, Search using "for" command

lista = [1, 2, 3, 4, 7, 8, 9, 11, 12, 13, 16, 17, 18, 20]
p = int(input("Escolha um número qualquer de 0 a 20: "))

for e in lista:
    if e == p:
        print("Elemento encontrado!")
        break

else:
    print("Elemento não encontrado.")