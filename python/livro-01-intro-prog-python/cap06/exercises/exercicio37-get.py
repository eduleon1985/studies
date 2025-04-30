### PT-BR (🇧🇷): 
# Crie um dicionário chamado produto, contendo os seguintes dados:
#   "nome": nome do produto
#   "preco": valor do produto
# Peça ao usuário que digite o nome de uma chave para consultar no dicionário. 
# Use o método .get() para exibir o valor da chave, ou uma mensagem como "Informação indisponível" caso a chave não exista.



### EN (🇺🇸):
# Create a dictionary called produto, containing the following data:
#   "nome": product name
#   "preco": product price
# Ask the user to type the name of a key to search in the dictionary. 
# Use the .get() method to display the value of the key or show a message like "Information not available" if the key does not exist.

produto = {
    "nome": "Camiseta",
    "preco": 39.90,
    "marca": "Nike",
    "tamanho": "G"
}

chave = input("Qual informação deseja consultar? (nome, preco...) - ")

valor = produto.get(chave, "Informação indisponível!")

print(valor)