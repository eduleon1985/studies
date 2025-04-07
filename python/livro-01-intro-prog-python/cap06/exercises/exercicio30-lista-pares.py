# PT-BR:
# Crie uma lista com vários números inteiros. 
# Em seguida, percorra a lista e crie uma nova lista contendo apenas os números pares. 
# Ao final, exiba a nova lista com os pares encontrados.

# EN:
# Create a list with several integers. 
# Then, loop through the list and build a new list containing only the even numbers. 
# Finally, print the list with the even numbers found.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22, 23, 24, 73, 74, 75, 76, 77, 91, 92, 93, 94]
lista_pares = []

print(lista)
print(lista_pares)

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)

print(lista_pares)