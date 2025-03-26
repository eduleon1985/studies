compras = []

while True:
    produto = input("Produto, ('fim' para sair): ")
    if produto == "fim":
        break
    compras.append(produto)

print("=" * 20)
for p in compras:
    print(p)
print("=" * 20)