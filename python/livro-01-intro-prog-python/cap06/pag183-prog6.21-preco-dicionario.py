tabela = {
    "Alface" : 0.45,
    "Cenoura" : 0.33,
    "Pimentão" : 1.27,
    "Banana" : 0.69,
    "Laranja" : 0.73,
    "Maçã" : 2.30,
    "Pêra" : 2.59,
    "Melancia" : 0.23,
    "Maracujá" : 4.99
}

while True:
    produto = input("Digite o nome do produto, 'fim' para término: ")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço: {tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado.")