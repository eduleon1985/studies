compras = []

while True:
    produto = input("Informe o produto (fim para sair): ")
    if produto == "fim":
        break

    quantidade = int(input("Informe a quantidade: "))
    preco = float(input("Informe o preço: R$ "))

    compras.append([produto, quantidade, preco])

soma = 0

for e in compras:
    print(f"{e[0]:20s} - {e[1]:5d} {e[2]:5.2f} {e[1]} * {e[2]:6.2f}")
    soma += e[1] * e[2]

print(f"Total: R$ {soma:2f}")