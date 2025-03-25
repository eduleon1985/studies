# Verifique o menor valor de um item numa lista

L = [8, 3, 6, 10, 78, 18, 29, 38, 77, 81, 94, 113, 141, 418, 2]

menor = L[0]
for i in L:
    if i < menor:
        menor = i

print(f"O menor valor da lista é o {menor}")