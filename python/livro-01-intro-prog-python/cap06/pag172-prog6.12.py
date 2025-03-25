# Cópia de elementos para outras listas

valores = [9, 8, 7, 12, 0, 13, 21, 14, 37, 84, 91, 33, 28, 15, 83, 285, 324]

pares = []
impares = []

for e in valores:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")