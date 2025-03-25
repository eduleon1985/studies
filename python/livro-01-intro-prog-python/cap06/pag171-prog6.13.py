T = [-10, -8, 0, 1, 2, 5, -2, -4]

maximo = T[0]
minimo = T[0]
for i in T:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i

print(f"A maior temperatura é {maximo}ºC.")
print(f"A menor temperatura é {minimo}ºC.")