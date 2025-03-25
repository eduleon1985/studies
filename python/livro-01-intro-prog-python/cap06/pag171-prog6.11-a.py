# Verifique o maior valor de um item numa lista

L = [8, 3, 6, 10, 78, 18, 29, 38, 77, 81, 94, 113, 141, 418, 2]

maximo = L[0]
for i in L:
    if i > maximo:
        maximo = i

print(f"O maior valor da lista é o {maximo}")