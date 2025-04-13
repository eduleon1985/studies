estoque = {
    "tomate": [1000, 2.30],
    "batata": [2001, 1.20],
    "alface": [500, 0.45],
    "feijão": [100, 1.50]
}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0

print("Vendas: \n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade

    print(f"{produto:12s}: {quantidade:3d} x R${preco:6.2f} = R${custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total: R${total:21.2f}\n")
print("="* 20)
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: R$, {dados[1]:6.2f} \n")