# Enunciado em PT-BR:
# Crie uma lista de produtos, onde cada item é uma sublista com o nome do produto e um código alfanumérico de 3 letras (como "A1B").
# Em seguida, percorra a lista e exiba o nome do produto junto com cada caractere do código separadamente.

# Statement in EN:
# Create a product list, where each item is a sublist containing the product name and a 3-character alphanumeric code (e.g., "A1B"). 
# Then, loop through the list and print the product name along with each character in the code separately.

produtos = [
    ["Monitor", "X1B"],
    ["Teclado", "A2C"],
    ["Mouse", "P3D"],
    ["Tablet", "K4Q"],
    ["Standing-Desk", "M5W"]
]

for item in produtos:
    nome = item[0]
    codigo = item[1]
    print(f"{nome} - Código: {codigo[0]}, {codigo[1]}, {codigo[2]}")
    # print(f"{nome} - Código: {codigo[0]}, {codigo[1]}, {codigo[2]}, {codigo[3]}, {codigo[4]}")